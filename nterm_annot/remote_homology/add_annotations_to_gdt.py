import pandas as pd
import numpy as np

annotation_to_family = {"GOODBYE-LIKE": ["Goodbye", "NACHT_N"], "HELO-LIKE": ["Helo_like_N", "SesA"], "SESB-LIKE": ["Abhydro_lipase", "Abhydrolase_1", "Abhydrolase_2", "Abhydrolase_3", "Abhydrolase_4", "Abhydrolase_5", "Abhydrolase_6", "Abhydrolase_7", "Abhydrolase_8", "Abhydrolase_9", "Acyl_transf_2", "Asp2", "AXE1", "BAAT_C", "Chlorophyllase", "Chlorophyllase2", "COesterase", "Cutinase", "DLH", "DUF1057", "DUF1100", "DUF1350", "DUF1400", "DUF1749", "DUF2048", "DUF2235", "DUF2920", "DUF2974", "DUF3089", "DUF3141", "DUF3530", "DUF452", "DUF676", "DUF726", "DUF818", "DUF829", "DUF900", "DUF915", "EHN", "Esterase", "Esterase_PHB", "FSH1", "Hydrolase_4", "LCAT", "LIDHydrolase", "LIP", "Lipase", "Lipase3_N", "Lipase_2", "Lipase_3", "Ndr", "PAE", "PAF-AH_p_II", "Palm_thioest", "PE-PPE", "Peptidase_S10", "Peptidase_S15", "Peptidase_S28", "Peptidase_S37", "Peptidase_S9", "PGAP1", "PhaC_N", "PHB_depo_C", "PhoPQ_related", "Say1_Mug180", "Ser_hydrolase", "Tannase", "Thioesterase", "UPF0227", "VirJ"], "PNP_UDP": "PNP_UDP_1", "HET": "HET", "PATATIN": ["Acyl_transf_1", "Patatin", "PLA2_B", "SAT"], "HELO": "HELO", "PFD-LIKE": ["HET-S", "NACHT_sigma", "Ses_B"], "C2": "C2", "RELA_SPOT": "RelA_SpoT", "CHAT": "CHAT", "PEPTIDASE_S8": "Peptidase_S8", "PKINASE": ["ABC1", "AceK", "Act-Frag_cataly", "Alpha_kinase", "APH", "APH_6_hur", "Choline_kinase", "CotH", "DUF1679", "DUF2252", "DUF4135", "EcKinase", "Fam20C", "Fructosamin_kin", "FTA2", "Haspin_kinase", "HipA_C", "Ins_P5_2-kin", "IPK", "IucA_IucC", "Kdo", "Kinase-like", "Kinase-PolyVal", "KIND", "Pan3_PK", "PI3_PI4_kinase", "PIP49_C", "PIP5K", "PK_Tyr_Ser-Thr", "Pkinase", "Pkinase_fungal", "Pox_ser-thr_kin", "RIO1", "Seadorna_VP7", "UL97", "WaaY", "YrbL-PhoP_reg", "YukC"], "TIR": ["TIR", "TIR_2"]}

family_to_annotation = {}
for k, v in annotation_to_family.items():
    if isinstance(v, list):
        for i in v:
            family_to_annotation[i] = k
    else:
        family_to_annotation[v] = k

annotation_table = pd.read_csv("remote_homologue_annotations_001.tsv", sep='\t').drop(["Nterm", "E-value"], axis=1)
annotation_table["Family/annotation"] = annotation_table["Family/annotation"].map(family_to_annotation)

gdt_file = pd.read_csv("Sep18p.i2.curated.arch.Ad44", sep='\t', names=["Representative no", "Nterm", "NOD", "Cterm"], header=None)

annotations_added = pd.merge(gdt_file, annotation_table, how="left")
annotations_added["Nterm"] = annotations_added["Nterm"].where(annotations_added["Nterm"] != "unk", annotations_added["Family/annotation"])
annotations_added_final = annotations_added.drop(["Family/annotation"], axis=1).fillna("unk")

annotations_added_final.to_csv("w_remhom_Sep18p.i2.curated.arch.Ad44", sep='\t', index=False, header=False)