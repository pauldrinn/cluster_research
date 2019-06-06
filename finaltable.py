import csv
import numpy as np 
import pandas

with open('test2', 'r') as f:
	reader = csv.reader(f, delimiter = '\t')
	with open('ttest.csv', 'w') as n:
		writer = csv.writer(n, delimiter = ',')
		writer.writerow(['Cluster'] + ['TA'])
		for row in reader:
			writer.writerow([row[1]] + [row[2]])

df = pandas.read_csv('ttest.csv') 
table = pandas.crosstab(df['Cluster'],df['TA']) 

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
rowwavg = pandas.Series(temprowwavg, name='rowweightedavg', index=[table.index[0]]); print(rowwavg)
colwavg = pandas.Series(tempcolwavg, name='colweightedavg', index=[table.columns[0]]); print(colwavg)

wrows = table.assign(rowmax = rowmax); #print(rowmax)
wcols = wrows.append(colmax)
wrows2 = wcols.assign(rowsum = rowsum)
wcols2 = wrows2.append(colsum)
wrows3 = wcols2.assign(rowpercent = rowpercent)
wcols3 = wrows3.append(colpercent)
wrows4 = wcols3.assign(rowweightedavg = rowwavg)
wcols4 = wrows4.append(colwavg)

wcols4.to_csv('newtable.csv', sep='\t')

print(wcols4.index[0])
print(wcols4.columns[0])