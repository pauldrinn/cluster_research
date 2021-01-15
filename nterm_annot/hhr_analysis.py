import os
import pandas as pd
import sys

init_df = pd.DataFrame()

hhr_dir = sys.argv[1]
for file in os.scandir(hhr_dir):
	if file.path.endswith(".hhr") and file.is_file():
		hhr_table = pd.read_fwf(file, skiprows=8, nrows=10, header=0, widths=[3, 32, 5, 8, 8, 7, 6, 5, 10, 15])
		hhr_table.set_index([pd.Index([os.path.basename(file).rsplit('_', 1)[0]] * hhr_table.shape[0], name='Cluster no'), 'No'], inplace=True)
		init_df = pd.concat([init_df, hhr_table])

init_df.to_csv(hhr_dir + '/' + 'results.tsv', sep='\t')