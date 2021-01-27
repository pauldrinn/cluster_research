# Notebook

## 27.01.2021

Fixed the table from before. Here is the final form (except the zinc finger annotation. Trying to figure that out.):

| Annotation             | Count |
|------------------------|-------|
| GOODBYE-LIKE           | 5471  |
| HELO-LIKE              | 4412  |
| PUP                    | 3422  |
| SESB-LIKE              | 3065  |
| unk                    | 2677  |
| HET                    | 878   |
| PATATIN                | 686   |
| C2 GOODBYE-LIKE        | 581   |
| HELO                   | 274   |
| PFD-LIKE               | 94    |
| NOA36                  | 49    |
| zf-Mss51 GOODBYE-LIKE  | 32    |
| TIR                    | 29    |
| SAM_Ste50p             | 24    |
| PEPTIDASE_S8           | 22    |
| PUP GOODBYE-LIKE       | 22    |
| SESB-LIKE GOODBYE-LIKE | 20    |

---
Added some more data to the table. Also received the phylogenetic data and edited it a bit, then added class data to the table as well -- which classes are present in the cluster and the number of classes as well.

## 25-26.01.2021

Did other stuff.

## 23-24.01.2021

I've been working on supporting multi annotations (e.g. C2 GOODBYE-LIKE). I'm currently working on a jupyter notebook and I will commit when it's done.

Finally built the script, although I'm having problems with the ordering of annotations, going to try sorting by 'Query HMM' first.

I believe sorting by 'Query HMM' worked but there are still some problems:

| Annotation                    | Count |
|-------------------------------|-------|
| GOODBYE-LIKE                  | 3998  |
| HELO-LIKE                     | 3547  |
| PUP ATPase_2                  | 3375  |
| SESB-LIKE                     | 3065  |
| unk                           | 2608  |
| HET                           | 878   |
| PATATIN                       | 686   |
| HELO-LIKE NACHT               | 584   |
| C2 GOODBYE-LIKE               | 581   |
| AAA_16                        | 547   |
| GOODBYE-LIKE NACHT            | 508   |
| GOODBYE-LIKE ATPase_2         | 427   |
| HELO-LIKE HELO                | 204   |
| HELO-LIKE HELO Zeta_toxin     | 182   |
| GOODBYE-LIKE HELO-LIKE AAA_16 | 106   |
| PFD-LIKE                      | 94    |
| GOODBYE-LIKE Bac_DnaA         | 53    |
| NOA36                         | 49    |
| PUP                           | 47    |
| GOODBYE-LIKE NB-ARC           | 44    |
| zf-Mss51 GOODBYE-LIKE         | 32    |
| TIR                           | 29    |
| GOODBYE-LIKE HELO-LIKE        | 26    |
| SAM_Ste50p                    | 24    |
| PUP GOODBYE-LIKE              | 22    |
| PEPTIDASE_S8                  | 22    |
| SESB-LIKE GOODBYE-LIKE        | 20    |

## 22.01.2021

Got to work but I realized I need to check for multiple annotations within the N-terminus.

Build three levels of tables: sequence level, cluster level, bin level. Obtained a somewhat good looking table in the end.

| bin             | Median sequence length before | Median sequence length after | Mean sequence length before | Mean sequence length after | Total number of sequences before | Total number of sequences after | Number of unknowns before | Number of unknowns after | Number of clusters before | Number of clusters after | Number of clusters with unknown(s)   before | Number of clusters with unknown(s)   after |
|-----------------|-------------------------------|------------------------------|-----------------------------|----------------------------|----------------------------------|---------------------------------|---------------------------|--------------------------|---------------------------|--------------------------|---------------------------------------------|--------------------------------------------|
| [1, 2)          | 125                           | 0                            | 213                         | 0                          | 4663                             | 0                               | 3320                      | 0                        | 4663                      | 0                        | 3320                                        | 0                                          |
| [2, 3)          | 146                           | 0                            | 223                         | 0                          | 1508                             | 0                               | 1028                      | 0                        | 754                       | 0                        | 536                                         | 0                                          |
| [3, 6)          | 142                           | 0                            | 212                         | 0                          | 1890                             | 0                               | 1279                      | 0                        | 528                       | 0                        | 389                                         | 0                                          |
| [6, 11)         | 168                           | 0                            | 206                         | 0                          | 1484                             | 0                               | 939                       | 0                        | 198                       | 0                        | 142                                         | 0                                          |
| [11, 21)        | 199                           | 58                           | 226                         | 207                        | 1369                             | 140                             | 788                       | 80                       | 96                        | 7                        | 71                                          | 4                                          |
| [21, 51)        | 207                           | 207                          | 218                         | 218                        | 2302                             | 2302                            | 1618                      | 910                      | 75                        | 75                       | 62                                          | 30                                         |
| [51, 101)       | 147                           | 147                          | 171                         | 171                        | 1423                             | 1423                            | 813                       | 697                      | 22                        | 22                       | 18                                          | 11                                         |
| [101,   201)    | 245                           | 245                          | 218                         | 218                        | 1301                             | 1301                            | 847                       | 443                      | 9                         | 9                        | 8                                           | 3                                          |
| [201,   501)    | 290                           | 290                          | 236                         | 236                        | 2264                             | 2264                            | 1458                      | 0                        | 6                         | 6                        | 6                                           | 0                                          |
| [501,   1001)   | 258                           | 258                          | 229                         | 229                        | 2304                             | 2304                            | 669                       | 547                      | 4                         | 4                        | 4                                           | 1                                          |
| [1001,   2001)  | 0                             | 0                            | 0                           | 0                          | 0                                | 0                               | 0                         | 0                        | 0                         | 0                        | 0                                           | 0                                          |
| [2001,   10001) | 345                           | 345                          | 330                         | 330                        | 12024                            | 12024                           | 1150                      | 0                        | 4                         | 4                        | 4                                           | 0                                          |

## 21.01.2021

Meeting done. Now I need to gather a lot of data and present it in a readable way. First, for bins (cluster size range) then for all clusters which will act as a template for the data presented in the publication. This version will be more detailed and cuts can be done later on. Oh and I should organize more of the code.

## 20.01.2021

If the minimum # of sequences in a cluster were 10 instead of 20, we would have 7479 unknowns before annotating (up by 826 from 6653).

## 19.01.2021

Did a few things. Added the option of not merging annotations (adding predicted and gdt annotations to separate columns) and extracted a table of tentatives.

Now, I want to align C2 (and C2-C2_1) and ALS2CR11 to see if they're homologues. I found out hhalign doesn't support HMMER profiles so I will have to use hhmake from seed alignments.

Seed alignments are in Stockholm format so used reformat.pl to convert them into a3m. Used hhmake to build .hhm profiles from a3m. Used hhalign to align them. Not sure about what the results mean. E-mailed advisor about this.

---
To-do for later:
- [ ] Note overlapping and conflicting hits (Not important)
- [x] (This is a problem since there are no C2 hits with GBL following it) Get all sequences with annotations of C2 and C2 + GBL into one big alignment and put them in something like FastTree
- [x] Get number of unknowns (according to the ground truth, gdt) in clusters with 10-19 sequences
- [x] Make histograms of:
    - [x] Number of sequences in clusters of particular size (# of sequences vs cluster size e.g. clusters with 11 sequences total 300 sequences)
    - [x] Number of unknown sequences (according to gdt) in clusters of particular size
- [ ] Get started on drawing domain with multiple annotations

## 18.01.2021

Didn't do much today, removed NOA36 from the tentative list and separated NUP from PNP_UDP, although some clusters are now mixed PNP_UDP_1 and NUP.

## 17.01.2021

Upgraded analysis script. Preliminary data:

- Number of unknowns in the GDT: **17462**
- Number of unknowns in the clusters before annotation: **6653** (so clustering and filtering clusters with less than 20 sequences and sequences with less than 20 residues removes **10809** unk sequences)
- Number of unknowns in the clusters after annotation (without tentatives): **3086** (**3567** sequences annotated almost certainly)
- Number of tentative annotations: **1506** (['Xin', 'SgrT', 'AAA_16', 'ALS2CR11', 'DUF2856'])
- Coverage: **20.43%** (w.r.t. unknowns in the GDT) and **53.61%** (w.r.t. unknowns in clusters >= 20 sequences)

In this coverage %, I included annotations with template HMM length of <= 50 and between E-value of 1 and 0.1 (but not in the tentative list above).

Cluster no|   No| Hit|  Prob|  E-value|   P-value|  Score|   SS|  Cols| Query HMM| Template HMM|
----------|-----|----|------|---------|----------|-------|-----|------|----------|-------------|
XP_007693719| 1|   PF17108.5 ; HET-S ; N-terminal|  65.5|     0.32|  0.000058|   21.5|  0.0|    20|     33-52|   2-21  (23)
OSS51700|     1|   PF17046.5 ; Ses_B ; SesB domai|  69.4|     0.22|  0.000043|  22.9|  0.0|    23|     19-41|   4-27  (28)
PWW75243|     1|   PF17106.5 ; NACHT_sigma ; Sigm|  67.3|     0.26|  0.000051|   24.2|  0.0|    24|     32-55|  17-40  (43)

- XP_007693719 has 41 sequences, 
- OSS51700 has 29 sequences and 
- PWW75243 has 39 sequences; 
    - totaling **109** (**745** with tentatives) from being a little more liberal with including annotations with template HMM length of <= 50 and between E-value of 1 and 0.1. 

## 16.01.2021

Committing new analysis script. It's still kinda messy atm but I will work on it more later. Also, I think I'll have to remove some annotations I added just because they were the top hit (below E-value of 0.1).

## 15.01.2021

Meeting over. We now have meaningful data but we need to extract the meaning now. A few things to include in the data to be presented to biologists:
- \# of seqs (in a cluster)
- \# of unk annotations (in a cluster), so makes sense to add an unk ratio column.
- Annotations, before and after (of all domains)
- Pfam clan if it's in a clan to discard less probable hits if hits are in the same clan.
- Taxonomic IDs, class names extracted from Dr. Dyrka's DB
- Coverage % (unk ratio of GDT / unk ratio of predicted label file -- updated from GDT)

Also, further filtering of hits should be done: (did this on 17.01.2021)
- For hits of longer alignments and high number of match states in the database HMM, any E-value more than 0.1 is considered useless in this case.
- For shorter ones, the E-value threshold is 1.

---
Trying out new things. It's my first time using argparser and finally putting everything into functions. Also implementing more error control.

## 12-14.01.2021

Did nothing. Meeting tomorrow to discuss the results and talk about what's next.

To-do for later:
- [ ] Turn everything into functions, use argparse and add ifnames.
- [x] Create function to add annotations found with extend_annot.py to a new ground truth (maybe not so true) file. (from 05.01.2021)
- [x] Same as #2 but with HHblits output so parsing .hhr must be done. I found a really well-written python gist but I'm thinking I should write it myself instead of using his.

## 11.01.2021

9am: That one cluster is still not done. There's probably something wrong.

---
3.35pm: Still wasn't done so I stopped it manually to try and empty space in my SSD and transfer the databases there.

Tried a test run of searching against Pfam with the HHblits output alignment from search against UniRef and cluster RFU34722.1 indeed found NACHT_N with 99.3% prob. and Goodbye with 99.2% prob. (ground truth annotation is GOODBYE-LIKE). Hit #3 was AAA with 82.8% prob. and looking at ground truth, some NOD annotations in this cluster are NACHT, AAA and unk so it's somewhat correct.

Another interesting point: apart from the first 2 hits which are indeed correct N-terminal annotations, the rest of the hits cover only a small (around 15 residues) amount at the end whereas the first two hits cover a much larger part (position 8 to 192), showing us obviously which hits are relevant.

---
5.45pm: Found out multithread.pl exists within HH-suite so I'll try that if searching from SSD takes too long. At the least, memory would be shared so other clusters can be done (alas won't really matter in my case since only 5 clusters remain BUT the pipeline would be much more performant with it).

One thing to note: [https://github.com/soedinglab/hh-suite/wiki#do-hhsearch-and-hhblits-work-fine-with-multi-domain-sequences](https://github.com/soedinglab/hh-suite/wiki#do-hhsearch-and-hhblits-work-fine-with-multi-domain-sequences)

Cluster RFU34722.1 got through prefiltering in iteration 2 this time and it's probably because it was on the SSD but the script dies during the realignment step which is probably caused by lack of RAM (lots of probabilities here).

---
XP_025168671.1 is a **really** interesting cluster. Its taxonomy is uncertain *(incertae sedis)* and most of the hits are uncharacterized proteins. Let's see what Pfam shows us.

---
One more cluster left (XP_024735629.1) and the process kills itself during (INFO: Realigning 42445 HMM-HMM alignments using Maximum Accuracy algorithm).
Found this issue: [https://github.com/soedinglab/hh-suite/issues/102](https://github.com/soedinglab/hh-suite/issues/102)
Upgrading from 12GB mem and 4GB swap to 12GB mem and 16GB swap.
Yep, turns out it's using all of the 12GB + 8GB out of the 16GB swap I allocated. Didn't take very long after this was solved.

---
Currently searching against Pfam. Some results make a lot of sense but some really don't. Looking forward to go through these with the professor.

```sh
bash nterm_annot/search_pipeline.sh minlen20_cluster_mode_1/UniRef30_2020_06 e_0.001_n_2_E_0.01_Z_1000000_M_50 pfam '-e 0.001 -n 1 -E 1 -Z 1000000' true
```
Search against Pfam was very fast, as expected.

NEW FAMILY??? PF09235.10: SAM_Ste50p isn't in the ground truth but it's 95.8% the annotation for cluster OCK94306.1. WOOOOOO I SEE SOOO MANY INTERESTING RESULTS AS I GO THROUGH MORE CLUSTERS!!!

The troublesome cluster (XP_024735629.1) has really weird annotations. They seem to be fungal but idk.

## 10.01.2021

10.20am: 105 out of 127 done.

---
11.50am: 111 out of 127 done. (Twice as fast? I guess there are a lot of factors at play here.)

As I get closer to the end, I am now starting to wonder if the output alignments will work for a second round of HHblits against Pfam. The reason I'm wondering is because the MPI toolkit version won't take my output file as input.

After a quick look at the HH-suite documentation, I'm fairly certain that it will work.

---
1.30pm: 115/127 done.

---
3.30pm: 117/127 done.

---
7.35pm: 122/127 done.

---
10.45pm: Iteration 2 prefiltering for Cluster XP_024735629.1 has been running since 6pm so that's about 5 hours (???)

---
I guess I'll leave it on for another night. That same cluster is still not done btw.

## 09.01.2021

Left HHblits pipeline running last night and so far at 12.28pm, 43 out of the 127 clusters went through the pipeline. I think RAM (I have 16GB of it) is the bottleneck here.

```sh
bash nterm_annot/search_pipeline.sh minlen20 cluster_mode_1 UniRef30_2020_06 '-e 0.001 -n 2 -E 0.01 -Z 1000000 -M 50'
```

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