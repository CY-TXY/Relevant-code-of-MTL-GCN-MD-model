import rdkit
from rdkit import Chem 
from rdkit.Chem import AllChem
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors import MoleculeDescriptors
import numpy as np
import os
import pandas as pd
dataset=pd.read_excel(...)
calc=MoleculeDescriptors.MolecularDescriptorCalculator([x[0] for x in Descriptors._descList])
Names=(calc.GetDescriptorNames())
def Partial_RDkit(smiles):
    mols= [Chem.MolFromSmiles(i) for i in smiles]
    calc=MoleculeDescriptors.MolecularDescriptorCalculator([x for x in Names])
    feature_names=Names
    Mol_descriptors=[]
    for mol in mols:
        mol=Chem.AddHs(mol)
        descriptors=calc.CalcDescriptors(mol)
        Mol_descriptors.append(descriptors)
    return Mol_descriptors,feature_names
Mol_descriptors,feature_names=Partial_RDkit(canon_smiles)
MD=pd.DataFrame(Mol_descriptors,columns=feature_names)
