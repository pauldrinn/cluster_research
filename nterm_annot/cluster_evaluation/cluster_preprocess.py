import pandas as pd
import sys

gdt_file_name = sys.argv[1] # Ground truth
clu_file_name = sys.argv[2] # Cluster file (.tsv)

gdt_file = pd.read_csv(gdt_file_name, sep='\t', names=["Representative no", "Nterm", "NOD", "Cterm"], header=None)
gdt_file = gdt_file.drop(["NOD", "Cterm"], axis = 1) # Dropping NOD and C-terminal

clu_file = pd.read_csv(clu_file_name, sep='\t', names=["Cluster no", "Representative no"], header=None)

gdt_file_wo_unk = gdt_file[~(gdt_file.Nterm.str.contains("unk"))].sort_values(by = 'Nterm', ignore_index = True) # Removing unknown entries
gdt_clu = pd.merge(gdt_file_wo_unk, clu_file) # Merging the ground truth and cluster file
gdt_clu = gdt_clu[['Representative no', 'Cluster no', 'Nterm']] # Reordering columns
gdt_clu['Nterm'] = gdt_clu['Nterm'].str.split().str[0] # Removing multiple annotations

gdt_clu.to_csv("mem_clu_ann.tsv", sep='\t', header=False, index=False)