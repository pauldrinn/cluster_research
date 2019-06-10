import csv
import numpy as np
import os
import pandas
flist =[]
[flist.append(f.replace('.xml','')) for f in os.listdir('./hmmprofiles') if not f.endswith('.hmm')]
flist.sort()

ddata = ['Total #seq. elements','Alignment length','# of unknowns','1st most abundant ann.','2nd most abundant ann.','3rd   most abundant ann.','Total hits','Eukaryote hits','Fungi hits','Hits (NACHT/NB-ARC)','1st most abundant pfam ann.','2nd most abundant pfam ann.','3rd most abundant pfam ann.']
table = pandas.DataFrame(index=flist,columns=ddata)

'''
for allfiles in os.listdir('./clustersfasta/hmmed'):
    if allfiles.endswith('aligned'): 
        with open('./clustersfasta/hmmed/'+allfiles,'r') as a:
            print a.readline()
'''
for allfiles in os.listdir('./clustersfasta/hmmed'):
    if allfiles.endswith('aligned'): 
        with open('./clustersfasta/hmmed/'+allfiles,'r') as a:
            stringy = a.read()
            dashes = stringy.count('-')
            annotations = stringy.count('>')
            print dashes
            print annotations
            '''
            for i, line in enumerate(a):
                if i==0:
                    print line
            '''


'''
def add_alignmentlen():
    for allfiles in os.listdir('./clustersfasta/hmmed'):
        if f.endswith('aligned'):
'''

#print(table)

#table.to_csv('./finaltable.csv')