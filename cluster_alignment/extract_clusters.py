import os
import sys

clu_all_seq = sys.argv[1]

if not os.path.exists('separated_clusters'):
    os.makedirs('separated_clusters')

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
				w = open('separated_clusters/' + previous[1:].strip() + '.fa', 'w')
			
			previous = identifier
		else:
			w.write(identifier + line)

# This part removes clusters with less than 20 members

	filelist = os.listdir('separated_clusters')
	for clufile in filelist:
		num_lines = sum(1 for line in open('separated_clusters/' + clufile))
		if num_lines < 42:
			os.remove('separated_clusters/' + clufile)