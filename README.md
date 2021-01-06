# Annotating N-terminal domains of NLRs in fungi based on remote homology

## Objective
Improving the coverage of annotations for N-terminal domains of NLR proteins.

## Approach

More detailed progress is available [here](docs/README.md)

### Through remote homologues (hmmsearch)
The relevant profiles were searched against our database and **1574** new domain annotations were obtained.

- [x] Pfam HMM library obtained ([ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz](http://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz))
- [x] Relevant families retrieved from https://doi.org/10.1007/978-3-030-49924-2_6 ([relevant_family_names.txt](data/remote_homology/relevant_family_names.txt))
- [x] Profile HMMs of relevant families fetched:
```sh
hmmfetch -f Pfam-A.hmm relevant_family_names.txt > relevant_pHMMs.hmm
```
- [x] Homology found using hmmsearch:
```sh
hmmsearch --tblout homologies.csv relevant_pHMMs.hmm ../Sep18p.curated.Ntm_env20_le10.fa
```
- [x] Families matched to annotations into [remote_homologue_annotations_001.tsv](data/remote_homology/remote_homologue_annotations_001.tsv) (inclusion threshold e-value: 0.01) with [annotate_homologues.py](nterm_annot/remote_homology/annotate_homologues.py)
- [x] Added new domain annotations to the ground truth file to obtain [w_remhom_Sep18p.i2.curated.arch.Ad44](data/remote_homology/w_remhom_Sep18p.i2.curated.arch.Ad44) 

### Through clustering and iterative search (jackhmmer)
- [x] Selected the best method of clustering (mmseqs2 --cluster-mode 1)
    - [x] Preprocessing of clustering results and analysis of clusters -- obtaining a score ([cluster_evaluation.py](nterm_annot/cluster_analysis.py))
- [x] Each cluster extracted into [separated_clusters](data/cluster_alignment/separated_clusters/) ([extract_clusters.py](nterm_annot/cluster_alignment/extract_clusters.py))
- [x] Clusters aligned into [aligned_clusters](data/cluster_alignment/aligned_clusters/) using Clustal Omega ([batch_alignment.sh](data/cluster_alignment/batch_alignment.sh))
- [ ] jackhmmer or hhsuite