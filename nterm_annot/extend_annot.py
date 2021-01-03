import os
import sys
import pandas as pd

clu_all_seq = "/home/paul/nterm_annot_project/data/clustering_outputs/env20_le10/minseqid_085_cluster_mode_1/clusters_all_seq.fasta" #sys.argv[1]
gdt = "/home/paul/nterm_annot_project/data/Sep18p.i2.curated.arch.Ad44" #sys.argv[2]

gdt_file = pd.read_csv(gdt, sep='\t', names=["Representative no", "Nterm", "NOD", "Cterm"], header=None)
gdt_file = gdt_file.drop(["NOD", "Cterm"], axis = 1) # Dropping NOD and C-terminal

#df = pd.DataFrame()

#previous = ''
with open(clu_all_seq, 'r') as f:
	for line in f:
		if line.startswith('>'): # /^'>/
			line_annot = gdt_file['Nterm'].loc[gdt_file['Representative no'] == line[1:].strip()].values[0]
			print(line[1:].strip(), "\t", line_annot)