import os
import pandas as pd

def hhr_to_df(hhr_path):
	"""Converts .hhr file(s) to pandas DataFrame and returns it
	
	Args:
		hhr_path (path-like): Path for a file or a directory. If it's a directory, function will convert all .hhr files in the directory into a single DataFrame.

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
		hhr_df = init_df
	elif os.path.isfile(hhr_path):
		if hhr_path.path.endswith(".hhr") and hhr_path.is_file():
			hhr_table = pd.read_fwf(hhr_path, skiprows=8, nrows=10, header=0, widths=[3, 32, 5, 8, 8, 7, 6, 5, 10, 15])
			hhr_table.set_index([pd.Index([os.path.basename(hhr_path).rsplit('_', 1)[0]] * hhr_table.shape[0], name='Cluster no'), 'No'], inplace=True)
			
			hhr_df = hhr_table
	else:
		raise TypeError('Input is neither a file nor a directory')
		
	return hhr_df

def get_template_hmm_len(df):
	"""Gets the template HMM length from a DataFrame created using hhr_to_df
	
	Args:
		df: Input DataFrame (output of function: hhr_to_df)
	
	Returns:
		Pandas Series object with template HMM lengths of all hits
	"""
	query_str = r'(?<=\()(.*?)(?=\))' # Explanation: (?<=\() is positive lookbehind for \( and (?=\) is positive lookahead for \)

	return df['Template HMM'].str.findall(query_str).str[0].astype('int32')

def filter_hits(df, column, threshold, threshold2=None, f_type=0, hmm_len=None, verbose=False):
	"""Filters a DataFrame created using hhr_to_df to remove hits worse than a threshold, or return hits between two thresholds.
	If column is 'E-value' or 'P-value', function will remove rows with a {E, P}-value higher than threshold; else function will remove rows with {Prob, Score} lower than threshold.

	Args:
		df (DataFrame): Input DataFrame (output of function: hhr_to_df) 
		column (str): {'E-value', 'P-value', 'Prob', 'Score'}
		threshold (int): Threshold for filtering
		threshold2 (int) (default: None): If hits within a range is wanted, threshold is best hit and threshold2 is worst hit.
		f_type (default: 0) (int): {0, 1}
			0: Filtering with regards to <column>, <threshold2> is used to get a range.
			1: Filtering with regards to <column> and with regards to <hmm_len>. Hits between two thresholds that have template HMM lengths below <hmm_len> will be included.
		hmm_len (default: None) (int): Template HMM length threshold.
		verbose (default: False) (bool): Print more details or not.
	
	Returns:
		Filtered pandas DataFrame object
	"""
	if f_type == 0:
		if hmm_len == None:
			if column in {'E-value', 'P-value'}:
				if threshold2 == None:
					filtered_df = df[df[column] < threshold]
				else:
					filtered_df = df[(df[column] >= threshold) & (df[column] < threshold2)]
			elif column in {'Prob', 'Score'}:
				if threshold2 == None:
					filtered_df = df[df[column] > threshold]
				else:
					filtered_df = df[(df[column] < threshold) & (df[column] >= threshold2)]
			else:
				raise TypeError('Only valid column names are Prob, Score, E-value and P-value. You tried to use {}.'.format(column))
		else:
			raise TypeError('Argument hmm_len can only be used with filtering type 1')
	elif f_type == 1:
		if isinstance(hmm_len, int):
			if column in {'E-value', 'P-value'}:
				filtered_hits = df[(get_template_hmm_len(df) <= hmm_len) & (df[column] >= threshold) & (df[column] < threshold2)]
				if verbose == True:
					print(filtered_hits)
					print('Adding {} hits with {}s between {} and {} and with a template HMM length of less than or equal to {} to the output DataFrame.'.format(filtered_hits.shape[0], column, threshold, threshold2, hmm_len))
				filtered_df = df[df[column] < threshold].append(filtered_hits)
			elif column in {'Prob', 'Score'}:
				filtered_hits = df[(get_template_hmm_len(df) <= hmm_len) & (df[column] < threshold) & (df[column] >= threshold2)]
				if verbose == True:
					print(filtered_hits)
					print('Adding {} hits with {}s between {} and {} and with a template HMM length of less than or equal to {} to the output DataFrame.'.format(filtered_hits.shape[0], column, threshold2, threshold, hmm_len))
				filtered_df = df[df[column] > threshold].append(filtered_hits)
			else:
				raise TypeError('Only valid column names are Prob, Score, E-value and P-value. You tried to use {}.'.format(column))
		elif isinstance(hmm_len, None):
			raise TypeError('Argument hmm_len must not be None with filtering type 1. hmm_len is the template HMM length threshold')
		else:
			raise TypeError('Argument hmm_len must be an int type. Type of your input is {}'.format(type(hmm_len)))
	else:
		raise TypeError('Only valid filtering types are 0 (which is the default) and 1 (which is more liberal, check help for more details on what this option does). You tried to use {}.'.format(f_type))
	
	return filtered_df

def update_table_annotations(annotations, table_file, merge=False, output_table_path=None):
	"""Updates annotations in a table with a supplied DataFrame or file (in the form of filter_hits output)

	Args:
		annotations: annotation file (tsv) or DataFrame object
		table_file: table (tsv) to update (actually creates a new table file; does not modify)
		output_table_path (default: None): output path if the dataframe is to be saved
	
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

	if merge == True:
		unk_table = table.query('`Nterm` == "unk"')
		copy_unk_table = unk_table.copy()

		copy_unk_table['Nterm'] = unk_table['Cluster no'].apply(lambda x: top_hits_local_annot.loc[x] if x in top_hits_local_annot else unk_table.loc[unk_table['Cluster no'] == x, 'Nterm'].iloc[0])
		table.update(copy_unk_table)
	elif merge == False:
		table['Nterm_GDT'] = table['Nterm']
		table['Nterm'] = table['Cluster no'].apply(lambda x: top_hits_local_annot.loc[x] if x in top_hits_local_annot else 'unk')

		# table['Nterm_merged'] = table['Cluster no'].apply(lambda x: top_hits_local_annot.loc[x] if x in top_hits_local_annot else table.loc[table['Cluster no'] == x, 'Nterm'].iloc[0])

	if output_table_path != None:
		table.to_csv(output_table_path, sep='\t', index=False)

	return table

def parse_args():
	import argparse
	try:
		parser = argparse.ArgumentParser(description='This script is used for extracting relevant (to me) information from HHblits output (.hhr file(s))')
		parser.add_argument('path', action='store', help='Input .hhr path')
	except:
		print('Please use the correct arguments')
	
	return parser.parse_args()

def main():
	args = parse_args()
	tentative_pfams = ['Xin', 'SgrT', 'AAA_16', 'DUF2856']

	hhr_df = hhr_to_df(args.path)
	if os.path.isdir(args.path):
		analysis_dir = os.path.join(args.path, 'analysis')
	elif os.path.isfile(args.ipath):
		analysis_dir = os.path.join(os.path.dirname(args.path), 'analysis')
	
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
	table_path = os.path.join(clu_outs_dir, 'minlen20', 'cluster_mode_1', 'clusters_table.tsv')

	updated_table = update_table_annotations(hhr_df_01, table_path, merge=False)
	updated_table['Nterm'] = updated_table.Nterm.replace(tentative_pfams, 'unk')
	updated_table.to_csv(os.path.join(analysis_dir, 'clusters_table_new.tsv'), sep='\t', index=False)

	liberal_hhr_df = filter_hits(hhr_df, 'E-value', 0.1, 1, 1, 50, True)
	liberal_table = update_table_annotations(liberal_hhr_df, table_path, merge=False)

	tentative_annot_count = liberal_table[liberal_table.Nterm.isin(tentative_pfams)].shape[0]

	liberal_table[liberal_table.Nterm.isin(tentative_pfams)].to_csv(os.path.join(analysis_dir, 'tentatives_table.tsv'), sep='\t')

	liberal_table['Nterm'] = liberal_table.Nterm.replace(tentative_pfams, 'unk')

	liberal_hhr_df.to_csv(os.path.join(analysis_dir, 'results_liberal.tsv'), sep='\t')
	liberal_table.to_csv(os.path.join(analysis_dir, 'clusters_table_new_liberal.tsv'), sep='\t', index=False)

	original_table = pd.read_csv(table_path, sep='\t')
	gdt_Nterms = pd.read_csv(os.path.join(root_dir, 'data', 'Sep18p.i2.curated.arch.Ad44'), sep='\t', header=None, usecols=[1])

	print('Number of unknowns in the GDT: {}'.format(gdt_Nterms[1].value_counts()['unk']))
	print('Number of unknowns in the clusters before annotation: {}'.format(original_table.Nterm.value_counts()['unk']))
	print('Number of unknowns in the clusters after annotation (without tentatives): {}'.format(liberal_table.Nterm.value_counts()['unk']))
	print('Number of tentative annotations: {}'.format(tentative_annot_count))
	
	new_annot_count = (original_table.Nterm.value_counts()['unk']) - (liberal_table.Nterm.value_counts()['unk'])
	coverage_from_gdt = ((new_annot_count / (gdt_Nterms[1].value_counts()['unk'])) * 100).round(2)
	coverage_from_clu = ((new_annot_count / (original_table.Nterm.value_counts()['unk'])) * 100).round(2)
	print("""Coverage: {}% (w.r.t. unknowns in the GDT) and 
	  {}% (w.r.t. unknowns in clusters >= 20 sequences)""".format(coverage_from_gdt, coverage_from_clu))

if __name__ == '__main__':
	main()