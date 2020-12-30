import pandas as pd

tblout = pd.read_csv("homologies.csv", delim_whitespace=True, comment='#', header=None).rename(columns={0:"Representative no", 2:"Family/annotation", 4:"E-value"})
tblout = tblout[["Representative no", "Family/annotation", "E-value"]]
tblout = tblout.sort_values('E-value', ascending=True).drop_duplicates('Representative no').sort_index().reset_index(drop=True) # Removes duplicates and keeps the lowest E-value annotation
tblout_001 = tblout[tblout["E-value"] < 0.01]

gdt_file = pd.read_csv("../Sep18p.i2.curated.arch.Ad44", sep='\t', names=["Representative no", "Nterm", "NOD", "Cterm"], header=None).drop(["NOD", "Cterm"], axis = 1)
gdt_file_unk = gdt_file[(gdt_file.Nterm.str.contains("unk"))].sort_values(by = 'Nterm', ignore_index = True)

gdt_tbl = pd.merge(gdt_file_unk, tblout)
gdt_tbl_001 = pd.merge(gdt_file_unk, tblout_001)

gdt_tbl.to_csv("remote_homologue_annotations.tsv", sep='\t', index=False)
gdt_tbl_001.to_csv("remote_homologue_annotations_001.tsv", sep='\t', index=False)