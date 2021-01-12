# Annotating N-terminal domains of NLRs in fungi based on remote homology

## Objective
Improving the coverage of annotations for N-terminal domains of NLR proteins.

## Approaches

More detailed progress is available [here](docs/README.md)

### Through *closer* homologues (only hmmsearch)
The relevant profiles were searched against our database and **1574** new domain annotations were obtained.

- Pfam HMM library obtained ([ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz](http://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz))
- Relevant families retrieved from https://doi.org/10.1007/978-3-030-49924-2_6 ([relevant_family_names.txt](data/remote_homology/relevant_family_names.txt))
- Profile HMMs of relevant families fetched:
```sh
hmmfetch -f Pfam-A.hmm relevant_family_names.txt > relevant_pHMMs.hmm
```
- Homology found using hmmsearch:
```sh
hmmsearch --tblout homologies.csv relevant_pHMMs.hmm Sep18p.curated.Ntm_env20_le10.fa
```
- Families matched to annotations into [remote_homologue_annotations_001.tsv](data/remote_homology/remote_homologue_annotations_001.tsv) (inclusion threshold e-value: 0.01) with [annotate_homologues.py](nterm_annot/remote_homology/annotate_homologues.py)
- Added new domain annotations to the ground truth file to obtain [w_remhom_Sep18p.i2.curated.arch.Ad44](data/remote_homology/w_remhom_Sep18p.i2.curated.arch.Ad44) 

### Through clustering and iterative remote homology search (mmseqs2 + HHblits)
- Selected the most relevant method of clustering (mmseqs2 --cluster-mode 1).
    - Preprocessing of clustering results and analysis of clusters -- obtaining a score ([cluster_evaluation.py](nterm_annot/cluster_evaluation.py)).
- Sequences clustered into databases and flat results with [clust_pipeline.sh](nterm_annot/clust_pipeline.sh).
- Clusters extracted into separate files and aligned to be used later in sequence searching using Clustal Omega with [align_pipeline.sh](nterm_annot/align_pipeline.sh).
- Alignments searched against UniRef30 in the first 2 iterations and against Pfam in the final iteration using HHblits ([search_pipeline.sh](nterm_annot/search_pipeline.sh)).

- Results to be analyzed in further detail.