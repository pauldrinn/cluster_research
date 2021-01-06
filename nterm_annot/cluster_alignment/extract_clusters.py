import os
import sys

clu_all_seq = sys.argv[1]
clus_dir = os.path.dirname(clu_all_seq)+ '/separated_clusters'

if not os.path.exists(clus_dir):
    os.makedirs(clus_dir)

previous = ''
with open(clu_all_seq, 'r') as f:
	for line in f:
		if line.startswith('>'): # /^'>/
			identifier = line
			if identifier == previous:
				try:
					w.close()
				except:
					pass
				w = open(clus_dir + '/' + previous[1:].strip() + '.fa', 'w')
			
			previous = identifier
		else:
			w.write(identifier + line)

"""
# Found out createseqfiledb does this with --min-sequences 20

# This part removes clusters with less than 20 members
filelist = os.listdir('separated_clusters')
for clufile in filelist:
	num_lines = sum(1 for line in open('separated_clusters/' + clufile))
	if num_lines < 42:
		os.remove('separated_clusters/' + clufile)
"""