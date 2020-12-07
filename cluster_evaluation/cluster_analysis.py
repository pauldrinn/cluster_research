import csv
import numpy as np 
import pandas as pd
import sys

mem_clu_ann = sys.argv[1]

df = pd.read_csv(mem_clu_ann, sep='\t', header=None)
df.drop(0, inplace=True, axis=1)
df.rename(columns={1: 'Cluster', 2: 'TA'}, inplace=True)

table = pd.crosstab(df['Cluster'],df['TA'])

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

table.assign(rowmax = rowmax).append(colmax).assign(rowsum = rowsum).append(colsum).assign(rowpercent = rowpercent).append(colpercent).assign(rowweightedavg = rowwavg).append(colwavg).to_csv(mem_clu_ann.rsplit('.',1)[0] + '_anal.tsv', sep='\t')

precision = rowwavg.iloc[0]
recall = colwavg.iloc[0]

print("Precision: {0}".format(precision.round(3)))
print("Recall: {0}".format(recall.round(3)))
print("F1 score: {0}".format(((2 * precision * recall)/(precision + recall)).round(3)))