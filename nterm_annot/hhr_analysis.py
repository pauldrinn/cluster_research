import os
import pandas as pd

def hhr_to_df(hhr_path):
	"""Converts .hhr file(s) to pandas DataFrame and returns it
	
	Args:
		hhr_path: Path for a file or a directory. If it's a directory, function will convert all .hhr files in the directory into a single DataFrame.

	Returns:
		A pandas DataFrame
	"""

	if os.path.isdir(hhr_path):
		init_df = pd.DataFrame()
		for file in os.scandir(hhr_path):
			if file.path.endswith(".hhr") and file.is_file():
				hhr_table = pd.read_fwf(file, skiprows=8, nrows=10, header=0, widths=[3, 32, 5, 8, 8, 7, 6, 5, 10, 15])
				hhr_table.set_index([pd.Index([os.path.basename(file).rsplit('_', 1)[0]] * hhr_table.shape[0], name='Cluster no'), 'No'], inplace=True)
				init_df = pd.concat([init_df, hhr_table])
		return init_df
	elif os.path.isfile(hhr_path):
		if hhr_path.path.endswith(".hhr") and hhr_path.is_file():
			hhr_table = pd.read_fwf(hhr_path, skiprows=8, nrows=10, header=0, widths=[3, 32, 5, 8, 8, 7, 6, 5, 10, 15])
			hhr_table.set_index([pd.Index([os.path.basename(hhr_path).rsplit('_', 1)[0]] * hhr_table.shape[0], name='Cluster no'), 'No'], inplace=True)
			return hhr_table

def filter_hits(df, column, threshold, threshold2=None):
	"""Filters a DataFrame created using hhr_to_df to remove hits worse than a threshold, or return hits between two thresholds.
	If column is 'E-value' or 'P-value', function will remove rows with a {E, P}-value higher than threshold; else function will remove rows with {Prob, Score} lower than threshold.

	Args:
		df: Input DataFrame (output of function: hhr_to_df) 
		column: {'E-value', 'P-value', 'Prob', 'Score'}
		threshold: Threshold for filtering
		threshold2 (optional): If hits within a range is wanted, threshold is best hit and threshold2 is worst hit.
	
	Returns:
		Filtered pandas DataFrame object
	"""
	if column in {'E-value', 'P-value'}:
		if threshold2 == None:
			return df[df[column] < threshold]
		else:
			return df[(df[column] >= threshold) & (df[column] < threshold2)]
	elif column in {'Prob', 'Score'}:
		if threshold2 == None:
			return df[df[column] > threshold]
		else:
			return df[(df[column] < threshold) & (df[column] >= threshold2)]
	else:
		raise TypeError('Only valid column names are Prob, Score, E-value and P-value. You used {}'.format(column))

def update_table_annotations(annotations, table_file, output_table_path):
	"""Updates annotations in a table with a supplied DataFrame or file (in the form of filter_hits output)

	Args:
		annotations: annotation file (tsv) or DataFrame object
		table_file: table (tsv) to update (actually creates a new table file; does not modify)
	
	Returns:
		DataFrame object with updated annotations (and creates a new file called *_new.tsv)
	"""
	table = pd.read_csv(table_file, sep='\t')
	table['Cluster no'] = table['Cluster no'].str.split('.').str[0]

	if isinstance(annotations, pd.DataFrame):
		annotations_df = annotations		
	elif os.path.isfile(annotations):
		annotations_df = pd.read_csv(annotations, sep='\t')

	from dicts import pfam_to_annot
	
	top_hits_df = annotations_df[annotations_df.index.get_level_values(1) == 1]
	top_hits = top_hits_df['Hit'].str.split(' ; ').str[1].droplevel(1)
	top_hits_local_annot = top_hits.replace(pfam_to_annot)
	
	unk_table = table.query('`Nterm` == "unk"')
	copy_unk_table = unk_table.copy()
	copy_unk_table['Nterm'] = unk_table['Cluster no'].apply(lambda x: top_hits_local_annot.loc[x] if x in top_hits_local_annot else unk_table.loc[unk_table['Cluster no'] == x, 'Nterm'].iloc[0])
	
	table.update(copy_unk_table)
	table.to_csv(output_table_path, sep='\t')
	return table

def parse_args():
	import argparse
	try:
		parser = argparse.ArgumentParser(description='This script is used for extracting relevant (to me) information from HHblits output (.hhr file(s))')
		parser.add_argument('-ip', '--inpath', action='store', help='Input .hhr path')
	except:
		print('Please use the correct arguments')
	
	return parser.parse_args()

def main():
	args = parse_args()

	hhr_df = hhr_to_df(args.inpath)
	if os.path.isdir(args.inpath):
		analysis_dir = os.path.join(args.inpath, 'analysis')
	elif os.path.isfile(args.ipath):
		analysis_dir = os.path.join(os.path.dirname(args.inpath), 'analysis')
	
	try: 
		os.mkdir(analysis_dir) 
	except OSError: 
		print('Analysis folder already exists, using it')
	
	hhr_df_01 = filter_hits(hhr_df, 'E-value', 0.1)
	hhr_df_1 = filter_hits(hhr_df, 'E-value', 1)
	
	hhr_df.to_csv(os.path.join(analysis_dir, 'results.tsv'), sep='\t')
	hhr_df_01.to_csv(os.path.join(analysis_dir, 'results_e-value_cutoff_0.1.tsv'), sep='\t')
	hhr_df_1.to_csv(os.path.join(analysis_dir, 'results_e-value_cutoff_1.tsv'), sep='\t')

	print("""No of hits with no e-val cutoff: {}, 
		e-val < 1: {}, 
		e-val < 0.1: {}"""
		.format(hhr_df.shape[0], hhr_df_1.shape[0], hhr_df_01.shape[0]))

	root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	clu_outs_dir = os.path.join(root_dir, 'data', 'clustering_outputs')

	update_table_annotations(hhr_df_01, os.path.join(clu_outs_dir, 'minlen20', 'cluster_mode_1', 'clusters_table.tsv'), os.path.join(analysis_dir, 'clusters_table_new.tsv'))

if __name__ == '__main__':
	main()