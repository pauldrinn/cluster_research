#!/bin/bash
# $1: mmseqs DB name (e.g. minlen20);
	# if $5 true: 'mmseqs DB name'_'mmseqs out DB name'/'HH-suite DB name' (e.g. minlen20_cluster_mode_1/UniRef30_2020_06)
# $2: mmseqs out DB name (e.g. cluster_mode_1);
	# if $5 true: 'HHblits parameters' of the run whose output will be used (e.g. e_0.001_n_2_E_0.01_Z_1000000_M_50)
# $3: HH-suite DB name (DB name inside ${DB_PATH})
# $4: HHblits parameters (as a string)
# $5: input is HHblits output (bool; false by default)
THIS_SCRIPT_DIR=$(dirname $(realpath ${BASH_SOURCE}))
source ${THIS_SCRIPT_DIR}/paths.sh

DB_PATH=/mnt/c/hhsuite_databases # EDIT THIS
THREADS=12 # EDIT THIS

TEMP_STRING=${4//" "/"_"}

if [ ! $5 ]
then
	OUTPUT_PATH=${DATA_DIR}/seq_searching/$1_$2/$3/"${TEMP_STRING//"-"/""}"
	INPUT_PATH=${DATA_DIR}/clustering_outputs/$1/$2/aligned_clusters
	INPUT_EXT=fa
else
	OUTPUT_PATH=${DATA_DIR}/seq_searching/Q_${1%%/*}_T_${1##*/}/$3/"${TEMP_STRING//"-"/""}"
	INPUT_PATH=${DATA_DIR}/seq_searching/$1/$2
	INPUT_EXT=a3m
fi

mkdir -p ${OUTPUT_PATH}

for FILE in ${INPUT_PATH}/*.${INPUT_EXT}; do
	NAME=${FILE##*/}
	HHR_OUTPUT=${OUTPUT_PATH}/${NAME%%.*}.hhr
	ALI_OUTPUT=${OUTPUT_PATH}/${NAME%%.*}.a3m
	echo "Searching ${NAME}"
	hhblits -i ${FILE} -o ${HHR_OUTPUT} -oa3m ${ALI_OUTPUT} -d ${DB_PATH}/$3 -cpu ${THREADS} $4
done