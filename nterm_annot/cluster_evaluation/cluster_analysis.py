import csv
import numpy as np 
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

df = gdt_clu.drop("Representative no", axis=1)

table = pd.crosstab(df['Cluster no'],df['Nterm'])

colmax = table.max(axis=0)				#max of columns (series)
colmax.name = 'colmax'
rowmax = table.max(axis=1)				#max of row		(series)

colsum = table.sum(axis=0)				#sum of columns (series)
colsum.name = 'colsum'										
rowsum = table.sum(axis=1)				#sum of rows	(series)

rowpercent = (rowmax/rowsum)*100
colpercent = (colmax/colsum)*100
colpercent.name = 'colpercent'

temprowwavg = (rowpercent * rowsum).sum() / rowsum.sum()
tempcolwavg = (colpercent * colsum).sum() / colsum.sum()
rowwavg = pd.Series(temprowwavg, name='rowweightedavg', index=[table.index[0]])
colwavg = pd.Series(tempcolwavg, name='colweightedavg', index=[table.columns[0]])

table.assign(rowmax = rowmax).append(colmax).assign(rowsum = rowsum).append(colsum).assign(rowpercent = rowpercent).append(colpercent).assign(rowweightedavg = rowwavg).append(colwavg).to_csv(clu_file_name.rsplit('.',1)[0] + '_anal.tsv', sep='\t')

precision = rowwavg.iloc[0]
recall = colwavg.iloc[0]

print("Precision: {0}".format(precision.round(3)))
print("Recall: {0}".format(recall.round(3)))
print("F1 score: {0}".format(((2 * precision * recall)/(precision + recall)).round(3)))