#!/bin/bash
# $1: gdt file 
# $2: db name 
# $3: clustering output 
# $4: clustering parameters
THIS_SCRIPT_DIR=$(dirname $(realpath ${BASH_SOURCE}))
source ${THIS_SCRIPT_DIR}/paths.sh

DB_DIR=${DATA_DIR}/dbs/$2_DB
DB=${DB_DIR}/$2_DB
OUT_DB_DIR=${DB_DIR}/out/$3
OUT_FILE_DIR=${DATA_DIR}/clustering_outputs/$2

mkdir -p ${DB_DIR} ${OUT_DB_DIR} ${OUT_FILE_DIR}/$3 ${OUT_DB_DIR}/seqdb
if [ ! -s ${DB} ]
then
	mmseqs createdb $(realpath $1) ${DB} --shuffle 0
fi
mmseqs cluster ${DB} ${OUT_DB_DIR}/$3_out_DB ${OUT_DB_DIR}/tmp $4
rm -r ${OUT_DB_DIR}/tmp

mmseqs createtsv ${DB} ${DB} ${OUT_DB_DIR}/$3_out_DB ${OUT_FILE_DIR}/$3/clusters.tsv
mmseqs createseqfiledb ${DB} ${OUT_DB_DIR}/$3_out_DB ${OUT_DB_DIR}/seqdb/$3_out_seq_DB # --min-sequences 20
mmseqs result2flat ${DB} ${DB} ${OUT_DB_DIR}/seqdb/$3_out_seq_DB ${OUT_FILE_DIR}/$3/clusters_all_seq.fasta