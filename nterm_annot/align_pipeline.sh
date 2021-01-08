#!/bin/bash
# $1: mmseqs DB name (e.g. minlen20)
# $2: mmseqs out DB name (e.g. cluster_mode_1)
THIS_SCRIPT_DIR=$(dirname $(realpath ${BASH_SOURCE}))
source ${THIS_SCRIPT_DIR}/paths.sh
CLU_ALL_DIR=${DATA_DIR}/clustering_outputs/$1/$2

mkdir -p ${CLU_ALL_DIR}/separated_clusters ${CLU_ALL_DIR}/aligned_clusters
python ${BIN_DIR}/extract_clusters.py ${CLU_ALL_DIR}/clusters_all_seq.fasta

for FILE in ${CLU_ALL_DIR}/separated_clusters/*.fa; do
	NAME="${FILE##*/}"
    OUTPUT="${CLU_ALL_DIR}/aligned_clusters/${NAME%%.*}_aligned.fa"
	clustalo -i ${FILE} -o "${OUTPUT}" --auto
    echo "${NAME} aligned"
done
