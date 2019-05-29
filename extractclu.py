import os
previous = ''
with open('iwantfasta.fa','r') as f:
	for line1 in f:
		line = line1.split()[0]
		if line[0]=='>':					# if ($1~"^>")
			identifier = line
			if identifier == previous:
				try:
					w.close()
				except:
					pass
  				w = open('clustersfasta/' + previous + '.fa','w')
			previous = identifier
		else:
			w.write(identifier + '\n' + line + '\n')
	filelist = os.listdir('clustersfasta')
	for clufile in filelist:
		num_lines = sum(1 for line in open('clustersfasta/' + clufile))
		if num_lines < 42:
			os.remove('clustersfasta/' + clufile)