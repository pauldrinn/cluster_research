ROOT_DIR := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
DATA_DIR := $(shell dirname $(ROOT_DIR))/data

PFAM_HMM_FILE_EXISTS := $(or $(and $(wildcard $(DATA_DIR)/remote_homology/Pfam-A.hmm),1),0)
PFAM_HMM_LINK := http://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz

.PHONY: all

all: check_pfam fetch_profile

# Remote homology

check_pfam:
ifeq ($(PFAM_HMM_FILE_EXISTS),1)
	@echo You seem to already have Pfam-A.hmm
else
	@echo "You don't have Pfam-A.hmm"
	@echo -n "Do you want to download Pfam-A.hmm? It's about 250MB and about 4-5 times bigger when extracted [y/N] " && read ans && [ $${ans:-N} = y ]
	@curl -o $(DATA_DIR)/remote_homology/Pfam-A.hmm.gz $(PFAM_HMM_LINK)
	@gzip -d $(DATA_DIR)/remote_homology/Pfam-A.hmm.gz
endif

fetch_profile:
	@hmmfetch --index $(DATA_DIR)/remote_homology/Pfam-A.hmm
	@hmmfetch -f $(DATA_DIR)/remote_homology/Pfam-A.hmm $(DATA_DIR)/remote_homology/relevant_family_names.txt > $(DATA_DIR)/remote_homology/relevant_pHMMs.hmm

# INCOMPLETE