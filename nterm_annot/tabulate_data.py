from Bio import SeqIO
import pandas as pd
import numpy as np

def tabulate_clusters():
	clu =  "/home/paul/nterm_annot_project/data/clustering_outputs/minlen20/cluster_mode_1/clusters_table_all.tsv"
	table =  "/home/paul/nterm_annot_project/data/seq_searching/Q_minlen20_cluster_mode_1_T_UniRef30_2020_06/pfam/e_0.001_n_1_E_1_Z_1000000/analysis/clusters_table_new_liberal.tsv"
	seqs = "/home/paul/nterm_annot_project/data/Sep18p.curated.Ntm_minlen20.fa"
	phylo = "/home/paul/nterm_annot_project/data/Sep18p.i2.curated.seqid_taxid_phylum_class_name.tsv"
	gdt = "/home/paul/nterm_annot_project/data/Sep18p.i2.curated.arch.Ad44"

	clu_file = pd.read_csv(clu, sep='\t', header=0, names=['cluster_no', 'identifier', 'nterm_gdt'])
	clu_file['cluster_no'] = clu_file['cluster_no'].str.split('.').str[0]

	table_file = pd.read_csv(table, sep='\t', header=0, names=['cluster_no', 'identifier', 'nterm', 'nterm_gdt'])
	phylo_file = pd.read_csv(phylo, sep='\t', header=None, names=['identifier', 'taxid', 'phylum', 'class', 'name'])
	gdt_file = pd.read_csv(gdt, sep='\t', header=None, names=['identifier', 'nterm_gdt', 'nod_gdt', 'cterm_gdt'])

	def get_seq_lens(file_path):
		with open(file_path) as f:
			ids = []
			seq_lens = []
			for record in SeqIO.parse(f, "fasta"):
				ids.append(record.id)
				seq_lens.append(len(record.seq))
		
		df = pd.DataFrame(data={'identifier': ids,'sequences_length': seq_lens})
		return df

	seq_lens_df = get_seq_lens(seqs)

	table1 = seq_lens_df.merge(table_file)
	table1['cluster_size'] = table1.groupby('cluster_no')['cluster_no'].transform('count')

	table2 = seq_lens_df.merge(clu_file)
	table2['cluster_size'] = table2.groupby('cluster_no')['cluster_no'].transform('count')

	after_annotation_df = pd.DataFrame()

	after_annotation_df['mean_seq_len'] = table1.groupby('cluster_no').mean()['sequences_length']
	after_annotation_df['median_seq_len'] = table1.groupby('cluster_no').median()['sequences_length']
	after_annotation_df['sum_residues'] = table1.groupby('cluster_no').sum()['sequences_length']

	before_annotation_df = pd.DataFrame()

	before_annotation_df['mean_seq_len'] = table2.groupby('cluster_no').mean()['sequences_length']
	before_annotation_df['median_seq_len'] = table2.groupby('cluster_no').median()['sequences_length']
	before_annotation_df['sum_residues'] = table2.groupby('cluster_no').sum()['sequences_length']

	unks_in_clusters_1 = table1.value_counts(['cluster_no', 'nterm'])[table1.value_counts(['cluster_no', 'nterm']).index.get_level_values(1) == 'unk'].reset_index(level=1, drop=True).reset_index().rename({0: 'unk_sequences'}, axis=1)
	unks_in_clusters_2 = table2.value_counts(['cluster_no', 'nterm_gdt'])[table2.value_counts(['cluster_no', 'nterm_gdt']).index.get_level_values(1) == 'unk'].reset_index(level=1, drop=True).reset_index().rename({0: 'unk_sequences'}, axis=1)

	after_annotation_df = after_annotation_df.reset_index().merge(unks_in_clusters_1, 'outer').replace({np.nan: 0}).round()
	after_annotation_df = after_annotation_df.merge(table1.drop(['identifier', 'sequences_length', 'nterm', 'nterm_gdt'], axis=1)).drop_duplicates().reset_index(drop=True)

	before_annotation_df = before_annotation_df.reset_index().merge(unks_in_clusters_2, 'outer').replace({np.nan: 0}).round()
	before_annotation_df = before_annotation_df.merge(table2.drop(['identifier', 'sequences_length', 'nterm_gdt'], axis=1)).drop_duplicates().reset_index(drop=True)

	after_annotation_df['has_unk'] = after_annotation_df['unk_sequences'] != 0
	before_annotation_df['has_unk'] = before_annotation_df['unk_sequences'] != 0

	after_annotation_df = after_annotation_df.merge(clu_file.groupby('cluster_no')['identifier'].apply(list).reset_index()).rename({'identifier': 'seq_ids'}, axis=1)
	before_annotation_df = before_annotation_df.merge(clu_file.groupby('cluster_no')['identifier'].apply(list).reset_index()).rename({'identifier': 'seq_ids'}, axis=1)

	before_phylogeny = table2[['identifier', 'cluster_no']].merge(phylo_file).drop(['identifier', 'taxid', 'phylum', 'name'], axis=1).drop_duplicates().groupby('cluster_no')['class'].apply(list).map(lambda x: [i.strip() for i in x]).reset_index()
	after_phylogeny = table1[['identifier', 'cluster_no']].merge(phylo_file).drop(['identifier', 'taxid', 'phylum', 'name'], axis=1).drop_duplicates().groupby('cluster_no')['class'].apply(list).map(lambda x: [i.strip() for i in x]).reset_index()

	#before_phylogeny['class'] = before_phylogeny['class'].str.strip()

	before_annotation_df = before_annotation_df.merge(before_phylogeny)
	after_annotation_df = after_annotation_df.merge(after_phylogeny)

	before_annotation_df['no_classes'] = before_annotation_df['class'].map(lambda x: len(x))
	after_annotation_df['no_classes'] = after_annotation_df['class'].map(lambda x: len(x))

	all_clusters_nterm_gdt = gdt_file.drop(['nod_gdt', 'cterm_gdt'], axis=1).drop_duplicates().reset_index(drop=True)
	all_clusters_nterm_gdt = clu_file.merge(all_clusters_nterm_gdt).drop(['identifier'], axis=1).drop_duplicates()
	all_clusters_nterm_gdt = all_clusters_nterm_gdt.groupby('cluster_no')['nterm_gdt'].apply(' '.join).reset_index()

	architectures = clu_file.merge(gdt_file).drop(['identifier'], axis=1).drop_duplicates().reset_index(drop=True)
	architectures['arch_gdt'] = architectures[['nterm_gdt', 'nod_gdt', 'cterm_gdt']].agg(list, axis=1)
	all_architectures = architectures.groupby('cluster_no')['arch_gdt'].apply(list).reset_index()

	after_nterm = table_file.drop(['identifier', 'nterm_gdt'], axis=1).drop_duplicates().reset_index(drop=True)
	after_annotation_df = after_annotation_df.merge(after_nterm)
	after_annotation_df = after_annotation_df.merge(all_clusters_nterm_gdt)
	before_annotation_df = before_annotation_df.merge(all_clusters_nterm_gdt)

	after_annotation_df = after_annotation_df.merge(all_architectures)
	before_annotation_df = before_annotation_df.merge(all_architectures)

	before_annotation_df['no_archs'] = before_annotation_df['arch_gdt'].map(lambda x: len(x))
	after_annotation_df['no_archs'] = after_annotation_df['arch_gdt'].map(lambda x: len(x))

	return before_annotation_df, after_annotation_df

def tabulate_to_bins(before_annotation_df, after_annotation_df, save_path=None):

	after_annotation_df['bin'] = pd.cut(after_annotation_df['cluster_size'], bins=[1,2,3,6,11,21,51,101,201,501,1001,2001,10001], right=False)
	before_annotation_df['bin'] = pd.cut(before_annotation_df['cluster_size'], bins=[1,2,3,6,11,21,51,101,201,501,1001,2001,10001], right=False)

	bins_df = pd.DataFrame()

	bins_df['before_median_seq_len'] = before_annotation_df.groupby('bin').median()['median_seq_len']
	bins_df['after_median_seq_len'] = after_annotation_df.groupby('bin').median()['median_seq_len']

	bins_df['before_mean_seq_len'] = before_annotation_df.groupby('bin').mean()['mean_seq_len']
	bins_df['after_mean_seq_len'] = after_annotation_df.groupby('bin').mean()['mean_seq_len']

	bins_df['before_sum_seq'] = before_annotation_df.groupby('bin').sum()['cluster_size']
	bins_df['after_sum_seq'] = after_annotation_df.groupby('bin').sum()['cluster_size']

	bins_df['before_sum_unk_seq'] = before_annotation_df.groupby('bin').sum()['unk_sequences']
	bins_df['after_sum_unk_seq'] = after_annotation_df.groupby('bin').sum()['unk_sequences']

	bins_df['before_no_clusters'] = before_annotation_df['bin'].value_counts().sort_index()
	bins_df['after_no_clusters'] = after_annotation_df['bin'].value_counts().sort_index()

	bins_df['before_no_clusters_w_unk'] = before_annotation_df.groupby('bin').sum()['has_unk']
	bins_df['after_no_clusters_w_unk'] = after_annotation_df.groupby('bin').sum()['has_unk']

	proper_names={'before_median_seq_len': 'Median sequence length before', 'after_median_seq_len': 'Median sequence length after', 'before_mean_seq_len': 'Mean sequence length before', 'after_mean_seq_len': 'Mean sequence length after', 'before_sum_seq': 'Total number of sequences before', 'after_sum_seq': 'Total number of sequences after', 'before_sum_unk_seq': 'Number of unknowns before', 'after_sum_unk_seq': 'Number of unknowns after', 'before_no_clusters': 'Number of clusters before', 'after_no_clusters': 'Number of clusters after', 'before_no_clusters_w_unk': 'Number of clusters with unknown(s) before', 'after_no_clusters_w_unk': 'Number of clusters with unknown(s) after'}

	bins_df = bins_df.replace({np.nan: 0}).round(1).rename(proper_names, axis=1)

	print(bins_df)

	if save_path != None:
		bins_df.to_csv(save_path, sep = '\t')


if __name__ == '__main__':
	b, a = tabulate_clusters()
	#tabulate_to_bins(b, a, 'test.tsv')

	#b.to_csv('/home/paul/nterm_annot_project/data/before_annotation.tsv', sep='\t')
	#a.to_csv('/home/paul/nterm_annot_project/data/after_annotation.tsv', sep='\t')

	print(b); print(a)