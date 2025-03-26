#!/usr/bin/env python
from Bio.PDB import PDBList

pdb_id = "2O8L"
pdbl = PDBList()
pdbl.retrieve_pdb_file(pdb_id, pdir="../data", file_format="pdb")