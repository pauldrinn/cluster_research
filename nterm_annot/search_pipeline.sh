#!/bin/bash
# $1: mmseqs DB name (e.g. minlen20)
# $2: mmseqs out DB name (e.g. cluster_mode_1)
# $3: HH-suite DB name (DB name inside ${DB_PATH})
# $4: HHblits parameters (as a string)
THIS_SCRIPT_DIR=$(dirname $(realpath ${BASH_SOURCE}))
source ${THIS_SCRIPT_DIR}/paths.sh

DB_PATH=/mnt/d/hhsuite_databases
THREADS=12 # EDIT THIS

TEMP_STRING=${4//" "/"_"}
OUTPUT_PATH=${DATA_DIR}/seq_searching/$1_$2/$3/"${TEMP_STRING//"-"/""}"
mkdir -p ${OUTPUT_PATH}

INPUT_PATH=${DATA_DIR}/clustering_outputs/$1/$2/aligned_clusters
for FILE in ${INPUT_PATH}/*.fa; do
	NAME=${FILE##*/}
    HHR_OUTPUT=${OUTPUT_PATH}/${NAME%%.*}.hhr
    ALI_OUTPUT=${OUTPUT_PATH}/${NAME%%.*}.a3m
    echo "Searching ${NAME}"
	hhblits -i ${FILE} -o ${HHR_OUTPUT} -oa3m ${ALI_OUTPUT} -d ${DB_PATH}/$3 -cpu ${THREADS} $4
done