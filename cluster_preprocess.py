import pandas as pd
import sys

gdt_file_name = sys.argv[1] # Ground truth
clu_file_name = sys.argv[2] # Cluster file (.tsv)

gdt_file = pd.read_csv(gdt_file_name, sep='\t', names=["Representative no", "Nterm", "NOD", "Cterm"], header=None)
gdt_file = gdt_file.drop(["NOD", "Cterm"], axis = 1) # Dropping NOD and C-terminal

clu_file = pd.read_csv(clu_file_name, sep='\t', names=["Cluster no", "Representative no"], header=None)

a = gdt_file[~(gdt_file.Nterm.str.contains("unk"))].sort_values(by = 'Nterm', ignore_index = True)
a = pd.merge(a, clu_file)
a = a[['Representative no', 'Cluster no', 'Nterm']]
a['Nterm'] = a['Nterm'].str.split().str[0]

a.to_csv("finalsort2", sep='\t', header=False, index=False)