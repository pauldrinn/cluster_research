import os
import sys
import pandas as pd

gdt =  sys.argv[1] #"/home/paul/nterm_annot_project/data/Sep18p.i2.curated.arch.Ad44"
clu =  sys.argv[2] #"/home/paul/nterm_annot_project/data/clustering_outputs/minlen20/cluster_mode_1/clusters.tsv"
save_dir = os.path.dirname(os.path.abspath(clu))
save_name = save_dir + '/' + os.path.basename(clu).rsplit('.', 1)[0] + '_table.tsv'
all_save_name = save_dir + '/' + os.path.basename(clu).rsplit('.', 1)[0] + '_table_all.tsv'

gdt_file = pd.read_csv(gdt, sep='\t', names=['Representative no', 'Nterm', 'NOD', 'Cterm'], header=None)
gdt_file = gdt_file.drop(['NOD', 'Cterm'], axis = 1) # Dropping NOD and C-terminal

clu_file = pd.read_csv(clu, sep='\t', header=None, names=['Cluster no', 'Representative no'])

clu_ann = clu_file.merge(gdt_file)
clu_ann['Cluster size'] = clu_ann.groupby('Cluster no')['Cluster no'].transform('count')

clu_ann_all = clu_ann.reset_index(drop=True).drop('Cluster size', axis=1)
clu_ann = clu_ann[clu_ann['Cluster size'] >= 20].reset_index(drop=True).drop('Cluster size', axis=1)

clu_ann_all.to_csv(all_save_name, sep='\t', index=False)
clu_ann.to_csv(save_name, sep='\t', index=False)

print('File saved to {}'.format(save_name),'\nThere are {} clusters with 20 or more sequences.\nThere are {} clusters in total.'.format(clu_ann['Cluster no'].unique().shape[0], clu_ann_all['Cluster no'].unique().shape[0]))