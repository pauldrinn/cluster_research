# Notebook

## 02.01.2020
Minor script edits. Pausing progress on Makefile for a while to focus on integrating mmseqs databases and obtaining results from minseqid 0.85.

---
Made folder data/dbs/ and new subfolder for each DB for minimum clutter. Can't decide on how to separate output DBs.

---
Decided to nest output DBs into the folders of their query database.

---
Created databases for raw FASTAs (pwd is data/):
```sh
mkdir -p dbs/env20_le10_DB dbs/minlen20_DB dbs/minlen30_DB
mmseqs createdb Sep18p.curated.Ntm_env20_le10.fa dbs/env20_le10_DB/env20_le10_DB --shuffle 0
mmseqs createdb Sep18p.curated.Ntm_minlen20.fa dbs/minlen20_DB/minlen20_DB --shuffle 0
mmseqs createdb Sep18p.curated.Ntm_minlen30.fa dbs/minlen30_DB/minlen30_DB --shuffle 0
```
Clustered the above FASTAs with connected component clustering (--cluster-mode 1) and deleted tmp folders manually (I don't think --remove-tmp-files works):
```sh
mkdir -p dbs/env20_le10_DB/out/cluster_mode_1_out dbs/minlen20_DB/out/cluster_mode_1_out dbs/minlen30_DB/out/cluster_mode_1_out
mmseqs cluster dbs/env20_le10_DB/env20_le10_DB dbs/env20_le10_DB/out/cluster_mode_1_out/cluster_mode_1_out_DB dbs/env20_le10_DB/out/cluster_mode_1_out/tmp --cluster-mode 1
mmseqs cluster dbs/minlen20_DB/minlen20_DB dbs/minlen20_DB/out/cluster_mode_1_out/cluster_mode_1_out_DB dbs/minlen20_DB/out/cluster_mode_1_out/tmp --cluster-mode 1
mmseqs cluster dbs/minlen30_DB/minlen30_DB dbs/minlen30_DB/out/cluster_mode_1_out/cluster_mode_1_out_DB dbs/minlen30_DB/out/cluster_mode_1_out/tmp --cluster-mode 1
```
Generated TSV formatted output of the clusterings.
```sh
mkdir -p clustering_outputs/env20_le10/cluster_mode_1 clustering_outputs/minlen20/cluster_mode_1 clustering_outputs/minlen30/cluster_mode_1
mmseqs createtsv dbs/env20_le10_DB/env20_le10_DB dbs/env20_le10_DB/env20_le10_DB dbs/env20_le10_DB/out/cluster_mode_1_out/cluster_mode_1_out_DB clustering_outputs/env20_le10/cluster_mode_1/clusters.tsv
mmseqs createtsv dbs/minlen20_DB/minlen20_DB dbs/minlen20_DB/minlen20_DB dbs/minlen20_DB/out/cluster_mode_1_out/cluster_mode_1_out_DB clustering_outputs/minlen20/cluster_mode_1/clusters.tsv
mmseqs createtsv dbs/minlen30_DB/minlen30_DB dbs/minlen30_DB/minlen30_DB dbs/minlen30_DB/out/cluster_mode_1_out/cluster_mode_1_out_DB clustering_outputs/minlen30/cluster_mode_1/clusters.tsv
```
Created sequence DBs of the clusterings for FASTA-like output. Clusters with less than 20 sequences are discarded thanks to --min-sequences 20. Previously, this was done by my script, extract_clusters.py.
```sh
mkdir -p dbs/env20_le10_DB/out/cluster_mode_1_out/seqdb dbs/minlen20_DB/out/cluster_mode_1_out/seqdb dbs/minlen30_DB/out/cluster_mode_1_out/seqdb
mmseqs createseqfiledb dbs/env20_le10_DB/env20_le10_DB dbs/env20_le10_DB/out/cluster_mode_1_out/cluster_mode_1_out_DB dbs/env20_le10_DB/out/cluster_mode_1_out/seqdb/cluster_mode_1_out_seq_DB --min-sequences 20
mmseqs createseqfiledb dbs/minlen20_DB/minlen20_DB dbs/minlen20_DB/out/cluster_mode_1_out/cluster_mode_1_out_DB dbs/minlen20_DB/out/cluster_mode_1_out/seqdb/cluster_mode_1_out_seq_DB --min-sequences 20
mmseqs createseqfiledb dbs/minlen30_DB/minlen30_DB dbs/minlen30_DB/out/cluster_mode_1_out/cluster_mode_1_out_DB dbs/minlen30_DB/out/cluster_mode_1_out/seqdb/cluster_mode_1_out_seq_DB --min-sequences 20
```
Generated FASTA-like output for the clusterings.
```sh
mmseqs result2flat dbs/env20_le10_DB/env20_le10_DB dbs/env20_le10_DB/env20_le10_DB dbs/env20_le10_DB/out/cluster_mode_1_out/seqdb/cluster_mode_1_out_seq_DB clustering_outputs/env20_le10/cluster_mode_1/clusters_all_seq.fasta
mmseqs result2flat dbs/minlen20_DB/minlen20_DB dbs/minlen20_DB/minlen20_DB dbs/minlen20_DB/out/cluster_mode_1_out/seqdb/cluster_mode_1_out_seq_DB clustering_outputs/minlen20/cluster_mode_1/clusters_all_seq.fasta
mmseqs result2flat dbs/minlen30_DB/minlen30_DB dbs/minlen30_DB/minlen30_DB dbs/minlen30_DB/out/cluster_mode_1_out/seqdb/cluster_mode_1_out_seq_DB clustering_outputs/minlen30/cluster_mode_1/clusters_all_seq.fasta
```
Next step (possibly) is to create a subpipeline that takes _all_seq.fasta and ground truth file as input and outputs a new ground truth file in which the annotation from one sequence of a cluster is extended to other sequences of the cluster.
I will try to do this without a pipeline first, then try to improve upon it.

---
Combined cluster_analysis.py and cluster_preprocess.py into a single script (cluster_analysis.py)

---
To-do:
- [] ~~Write a better way to discard clusters with less than n sequences.~~ Turns out, createseqfiledb does this already with --min-sequences while generating a FASTA-like output. 

## 01.01.2020
Happy new year! Day off. (Fixed ordering in this notebook phew)

## 31.12.2020
Procrastinated a lot. Learned about what a Makefile is. Loved it. Decided to use it. Currently trying to write one big Makefile to execute the pipeline I have in hand.

---
Making progress. Although not really necessary, I'm prompting the user to download Pfam-A.hmm to fetch profile HMMs from it for approach #1.

## 30.12.2020
Confused about why easy-cluster and cluster give me different results.

Figured out it's because createdb defaults to --shuffle 1 and db creation step in easy-cluster defaults to --shuffle 0 (I think? Documentation says otherwise but changing it to 0 gives me the same result as easy-cluster).

```sh
mmseqs createdb ../Sep18p.curated.Ntm_env20_le10.fa Sep18DB --shuffle 0
```

---
Trimmed the 20 residue envelope from every sequence and created 2 new FASTA files with minimum sequence length of 20 (Sep18p.curated.Ntm_minlen20.fa) and 30 (Sep18p.curated.Ntm_minlen30.fa) using seqkit.

```sh
cat Sep18p.curated.Ntm_env20_le10.fa | seqkit mutate -w 0 -d -20:-1 --quiet | seqkit seq -w 0 -m 20 > Sep18p.curated.Ntm_minlen20.fa
cat Sep18p.curated.Ntm_env20_le10.fa | seqkit mutate -w 0 -d -20:-1 --quiet | seqkit seq -w 0 -m 30 > Sep18p.curated.Ntm_minlen30.fa
```
A comparison:
|file                             | format |   type  | num_seqs |  sum_len  | min_len | avg_len | max_len |
|---------------------------------|--------|---------|----------|-----------|---------|---------|---------|
|Sep18p.curated.Ntm_env20_le10.fa | FASTA  | Protein |  36,134  | 9,187,203 |   20    |  254.3  |  5,731  |
|Sep18p.curated.Ntm_minlen20.fa   | FASTA  | Protein |  32,532  | 8,453,035 |   20    |  259.8  |  5,711  |
|Sep18p.curated.Ntm_minlen30.fa   | FASTA  | Protein |  31,756  | 8,433,921 |   30    |  265.6  |  5,711  |

---
Clustered minlen20 and minlen30 (--cluster-mode 1).

```sh
mmseqs cluster m20DB m20outDB tmp --cluster-mode 1
mmseqs cluster m30DB m30outDB tmp --cluster-mode 1
```

Results (although somewhat pointless):
- minlen20: 
    Precision: 99.715
    Recall: 67.97
    F1 score: 80.838
- minlen30:
    Precision: 99.715
    Recall: 62.033
    F1 score: 76.484

---
Thinking about switching to a src/ data/ structure (module-oriented?)

Attempted to switch to aforementioned structure (half-assed)

---
To-do for ~~tomorrow~~ later:
- [x] Integrate mmseqs databases (02.01.2021)
- [] Build better pipeline for multiple mmeqs databases and fix evaluation module (parameters and file naming).
- [x] Basically complete the structural reform (02.01.2021)