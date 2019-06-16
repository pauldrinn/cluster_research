import csv
from collections import Counter 
import numpy as np
import os
import pandas
#xmllist = [], [xmllist.append(f.replace('.xml','')) for f in os.listdir('./hmmprofiles') if not f.endswith('.hmm')], xmllist.sort()
alnfilelist = []
[alnfilelist.append(f.replace('.fa aligned','')) for f in os.listdir('./clustersfasta/hmmed') if not f.endswith('.fa')]
alnfilelist.sort()

ddata = ['Total #seq. elements','Alignment length','# of unknowns','1st most abundant ann.','2nd most abundant ann.','3rd most abundant ann.','Total hits','Eukaryote hits','Fungi hits','Hits (NACHT/NB-ARC)','1st most abundant pfam ann.','2nd most abundant pfam ann.','3rd most abundant pfam ann.']
table = pandas.DataFrame(index=alnfilelist,columns=ddata)

#adds alignment length
alnlendic = {}
for alnfile in alnfilelist:
	with open('./clustersfasta/hmmed/'+alnfile+'.fa aligned','r') as f:
		for i, line in enumerate(f):
			if i==2:
				alnlen = len(line)-1
		alnlendic.update({alnfile:alnlen})
for afile, alen in alnlendic.iteritems():
	table.loc[afile,'Alignment length'] = alen

#adds tot # of seq. elements
totseqelements = {}
for alnfile in alnfilelist:
	with open('./clustersfasta/hmmed/'+alnfile+'.fa aligned','r') as f:
		stringy = f.read()
		seqele = stringy.count('>')
		totseqelements.update({alnfile:seqele})
for afile, totseq in totseqelements.iteritems():
	table.loc[afile,'Total #seq. elements'] = totseq

#adds # of unk annotations
unkannotations = {}
gdtunk = []
with open('Sep18p.i2.curated.arch.Ad44') as gdtfile:
	reader = csv.reader(gdtfile, delimiter='\t')
	for row in reader:
		if (row[1] == "unk"):
			gdtunk.append(row[0])
for alnfile in alnfilelist:
	with open('./clustersfasta/hmmed/'+alnfile+'.fa aligned','r') as f:
		newf = f.read().split('\n')
		anninfile = []
		unkcount = 0
		for uid in newf:
			if uid.startswith('>'):
				anninfile.append(uid.split('>')[1])
		for i in anninfile:
			if i in gdtunk:
				unkcount +=1
		unkannotations.update({alnfile:unkcount})
for afile, nounk in unkannotations.iteritems():
	table.loc[afile,'# of unknowns'] = nounk

abundant1, abundant2, abundant3 = {}, {}, {}
gdtann = {}
with open('Sep18p.i2.curated.arch.Ad44') as gdtfile:
	reader = csv.reader(gdtfile, delimiter='\t')
	for row in reader:
		#if (row[1] != "unk"):
		gdtann.update({row[0]:row[1].split()[0]})

for alnfile in alnfilelist:
	with open('./clustersfasta/hmmed/'+alnfile+'.fa aligned','r') as f:
		newf = f.read().split('\n')
		anninfile = []
		c = Counter()
		for uid in newf:
			if uid.startswith('>'):
				anninfile.append(uid.split('>')[1])
		for i in anninfile:
			if i in gdtann:
				c[gdtann[i]] += 1
		mcommon = c.most_common(3)
		abundant1.update({alnfile:mcommon[0]})
		try:
			abundant2.update({alnfile:mcommon[1]})
		except:
			abundant2.update({alnfile:'None'})
		try:
			abundant3.update({alnfile:mcommon[2]})
		except:
			abundant3.update({alnfile:'None'})
for afile, abundancy1 in abundant1.iteritems():
	table.loc[afile,'1st most abundant ann.'] = abundancy1
for afile, abundancy2 in abundant2.iteritems():
	table.loc[afile,'2nd most abundant ann.'] = abundancy2
for afile, abundancy3 in abundant3.iteritems():
	table.loc[afile,'3rd most abundant ann.'] = abundancy3

table.to_csv('./finaltable.csv')