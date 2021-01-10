# Notebook

## 10.01.2021

10.20am: 105 out of 127 done.

---
11.50am: 111 out of 127 done. (Twice as fast? I guess there are a lot of factors at play here.)

## 09.01.2021

Left HHblits pipeline running last night and so far at 12.28pm, 43 out of the 127 clusters went through the pipeline. I think RAM (I have 16GB of it) is the bottleneck here.

---
4.20pm: 57 out of 127 done. Results are starting to make sense, just need to run em against Pfam for some proper annotations -- UniProt names alone don't tell us anything.

---
7.20pm: 63 out of 127 done.

---
10.20pm: 69 out of 127 done. Assuming the speed is somewhat constant, it should be done in 9 to 10 hours, so around 8-9am. Great!

## 08.01.2021

Had a meeting with Dr. Dyrka. We discussed the results and what to do next. I will be working with HHblits, searching cluster_mode_1 clustering of the minlen20 database against UniRef to obtain initial alignments which I will then run against Pfam for (possible) discovery of annotations. We are aware that some of the clusters won't have annotations so we are trying to extend the coverage of the annotations as much as we can and note what percentage we increased the coverage to.

I will create a new folder for HHblits searches I do and store all the alignments from the search against UniRef30.

---
Okay, so I have a bunch of subfolders and a pipeline script now. It all seems to work well EXCEPT how long HHblits takes. I will either buy a new SSD (I need a new NVMe drive anyway) or empty ~100GB from my current SSD which is a long shot. Apart from that, I just have to wait.

## 07.01.2021

I went over some of the results and I have so many questions.

## 06.01.2021

Downloading Pfam and UniRef30 for HH-suite.

---
The download is quite large so I wrote clust_pipeline.sh in the meanwhile (still extracting though). To-do item #1 done!

---
Still extracting UniRef30 after 45 minutes.

---
Took about 1.5 hours. It's now 180GB x| (from 46GB)
Ready to search but now I have to deal with extracting cluster sequences and aligning them. Will make new shell script called align_pipeline.

---
Wrote extraction & alignment pipeline, now trying searching.

Local HHblits against Pfam works well and quite fast, most likely because it's only 4GB big. BUT, just the prefiltering step alone takes longer than 20 minutes against UniRef30.

---
After about more than an hour, the search was complete and the results were indeed the same as the results from HHblits inside the MPI toolkit.
The slowness might be because of the database's location (HDD).
I will take care of the rest tomorrow.

## 05.01.2021

After spending an unhealthy amount of time with trying to read from FASTA-like output to create a table, I realized that I didn't need that AT ALL and that tsv output of mmseqs is even easier to work with since it comes somewhat tabular out of the box.

This is what the end result looks like. It's only the mmseqs tsv output inner merged with ground truth so what took me so long? I think I need to put more thought into things before diving headfirst. Also, pandas is **soooooooo** much faster compared to the native Python I/O. What a beautiful package.

|Cluster no	|Representative no|	  Nterm   |
|-----------|-----------------|-----------|
|ELR08403.1	|    ELR08403.1   | HELO-LIKE |
|ELR08403.1	|    ELR10080.1   | HELO-LIKE |
|ELR08403.1	|    KFY02009.1   | HELO-LIKE |
|ELR08403.1	|    KFY06076.1   | HELO-LIKE |
|   ...     |       ...       |    ...    |

---
To-do:
- [x] Still need to automate my mmseqs usage (somewhat like easy-cluster). Need a mix of createdb, cluster, createtsv (and createseqfiledb + result2flat if I need FASTA-like output at some point in the future). (06.01.2021)
- [x] Start homology searching. This should be interesting. (HHblits against Pfam and Uniclust30 with -M 50) (06.01.2021)
- [ ] Create function to add annotations found with extend_annot.py to a new ground truth (maybe not so true) file.

(I want to get all of these done by Thursday if not tomorrow!)

## 04.01.2021

Zoom call and no work.

## 03.01.2021

Fixed the dates on this notebook :p

---
Started clustering minimum sequence identity = 0.85 sets.
```sh
mkdir -p dbs/env20_le10_DB/out/minseqid_085_cluster_mode_1_out dbs/minlen20_DB/out/minseqid_085_cluster_mode_1_out dbs/minlen30_DB/out/minseqid_085_cluster_mode_1_out
mmseqs cluster dbs/env20_le10_DB/env20_le10_DB dbs/env20_le10_DB/out/minseqid_085_cluster_mode_1_out/minseqid_085_cluster_mode_1_out_DB dbs/env20_le10_DB/out/minseqid_085_cluster_mode_1_out/tmp --cluster-mode 1 --min-seq-id 0.85
mmseqs cluster dbs/minlen20_DB/minlen20_DB dbs/minlen20_DB/out/minseqid_085_cluster_mode_1_out/minseqid_085_cluster_mode_1_out_DB dbs/minlen20_DB/out/minseqid_085_cluster_mode_1_out/tmp --cluster-mode 1 --min-seq-id 0.85
mmseqs cluster dbs/minlen30_DB/minlen30_DB dbs/minlen30_DB/out/minseqid_085_cluster_mode_1_out/minseqid_085_cluster_mode_1_out_DB dbs/minlen30_DB/out/minseqid_085_cluster_mode_1_out/tmp --cluster-mode 1 --min-seq-id 0.85
```
Generated TSV formatted output of the clusterings.
```sh
mkdir -p clustering_outputs/env20_le10/minseqid_085_cluster_mode_1 clustering_outputs/minlen20/minseqid_085_cluster_mode_1 clustering_outputs/minlen30/minseqid_085_cluster_mode_1
mmseqs createtsv dbs/env20_le10_DB/env20_le10_DB dbs/env20_le10_DB/env20_le10_DB dbs/env20_le10_DB/out/minseqid_085_cluster_mode_1_out/minseqid_085_cluster_mode_1_out_DB clustering_outputs/env20_le10/minseqid_085_cluster_mode_1/clusters.tsv
mmseqs createtsv dbs/minlen20_DB/minlen20_DB dbs/minlen20_DB/minlen20_DB dbs/minlen20_DB/out/minseqid_085_cluster_mode_1_out/minseqid_085_cluster_mode_1_out_DB clustering_outputs/minlen20/minseqid_085_cluster_mode_1/clusters.tsv
mmseqs createtsv dbs/minlen30_DB/minlen30_DB dbs/minlen30_DB/minlen30_DB dbs/minlen30_DB/out/minseqid_085_cluster_mode_1_out/minseqid_085_cluster_mode_1_out_DB clustering_outputs/minlen30/minseqid_085_cluster_mode_1/clusters.tsv
```
Created sequence DBs of the clusterings for FASTA-like output. Clusters with less than 20 sequences are discarded.
```sh
mkdir -p dbs/env20_le10_DB/out/minseqid_085_cluster_mode_1_out/seqdb dbs/minlen20_DB/out/minseqid_085_cluster_mode_1_out/seqdb dbs/minlen30_DB/out/minseqid_085_cluster_mode_1_out/seqdb
mmseqs createseqfiledb dbs/env20_le10_DB/env20_le10_DB dbs/env20_le10_DB/out/minseqid_085_cluster_mode_1_out/minseqid_085_cluster_mode_1_out_DB dbs/env20_le10_DB/out/minseqid_085_cluster_mode_1_out/seqdb/minseqid_085_cluster_mode_1_out_seq_DB --min-sequences 20
mmseqs createseqfiledb dbs/minlen20_DB/minlen20_DB dbs/minlen20_DB/out/minseqid_085_cluster_mode_1_out/minseqid_085_cluster_mode_1_out_DB dbs/minlen20_DB/out/minseqid_085_cluster_mode_1_out/seqdb/minseqid_085_cluster_mode_1_out_seq_DB --min-sequences 20
mmseqs createseqfiledb dbs/minlen30_DB/minlen30_DB dbs/minlen30_DB/out/minseqid_085_cluster_mode_1_out/minseqid_085_cluster_mode_1_out_DB dbs/minlen30_DB/out/minseqid_085_cluster_mode_1_out/seqdb/minseqid_085_cluster_mode_1_out_seq_DB --min-sequences 20
```
Generated FASTA-like output for the clusterings.
```sh
mmseqs result2flat dbs/env20_le10_DB/env20_le10_DB dbs/env20_le10_DB/env20_le10_DB dbs/env20_le10_DB/out/minseqid_085_cluster_mode_1_out/seqdb/minseqid_085_cluster_mode_1_out_seq_DB clustering_outputs/env20_le10/minseqid_085_cluster_mode_1/clusters_all_seq.fasta
mmseqs result2flat dbs/minlen20_DB/minlen20_DB dbs/minlen20_DB/minlen20_DB dbs/minlen20_DB/out/minseqid_085_cluster_mode_1_out/seqdb/minseqid_085_cluster_mode_1_out_seq_DB clustering_outputs/minlen20/minseqid_085_cluster_mode_1/clusters_all_seq.fasta
mmseqs result2flat dbs/minlen30_DB/minlen30_DB dbs/minlen30_DB/minlen30_DB dbs/minlen30_DB/out/minseqid_085_cluster_mode_1_out/seqdb/minseqid_085_cluster_mode_1_out_seq_DB clustering_outputs/minlen30/minseqid_085_cluster_mode_1/clusters_all_seq.fasta
```
Obtained some results from --cluster-mode 1 --min-seq-id 0.85 clustering of env20_le10.
Out of 1017 sequences left after filtering small clusters (<20 sequences) and 39 remaining clusters, only 2 clusters had mixed results (unk + !unk) resulting in 27 new annotations (a mix of PNP-UDP and Goodbye-like).
There are 14762 unk annotations in the GDT file so 27 is just a drop in the ocean compared to the rest of the unknowns.

Need to investigate further, maybe with minimum sequence identity below 0.85 (around 0.75-0.8).
Also need to automate these results since I just counted them manually to check whether if it's similar to what was expected and it seems like it works well.

## 02.01.2021
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
- ~~[ ] Write a better way to discard clusters with less than n sequences.~~ Turns out, createseqfiledb does this already with --min-sequences while generating a FASTA-like output.
- [x] Take _all_seq.fasta and ground truth file as input and output a new ground truth file in which the annotation from one sequence of a cluster is extended to other sequences of the cluster. (05.01.2021 --I guess?--)

## 01.01.2021
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
- [x] Build better pipeline for multiple mmeqs databases and fix evaluation module (parameters and file naming). (03.01.2021)
- [x] Basically complete the structural reform (02.01.2021)