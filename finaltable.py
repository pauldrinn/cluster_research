import csv
import numpy as np
import os
import pandas
flist =[]
[flist.append(f.replace('.xml','')) for f in os.listdir('./hmmprofiles') if not f.endswith('.hmm')]
flist.sort()

ddata = ['Total #seq. elements','Alignment length','# of unknowns','Total hits','Eukaryote hits','Fungi hits','Hits (NACHT/NB-ARC)','1st most abundant pfam ann.','2nd most abundant pfam ann.','3rd most abundant pfam ann.']
#print flist
table = pandas.DataFrame(index=flist,columns=ddata)

print(table)

table.to_csv('./finaltable.csv')