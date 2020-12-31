# Notebook

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
- Integrate mmseqs databases
- Build better pipeline for multiple mmeqs databases and fix evaluation module (parameters and file naming).
- Basically complete the structural reform

## 31.12.2020

Procrastinated a lot. Learned about what a Makefile is. Loved it. Decided to use it. Currently trying to write one big Makefile to execute the pipeline I have in hand.

Making progress. Although not really necessary, I'm prompting the user to download Pfam-A.hmm to fetch profile HMMs from it for approach #1.