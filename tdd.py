import pytest
import bioinfo_dicts

def n_neg(seq):
    """Computes the number of negative residues in a protein sequence."""

    # Convert to uppercase
    seq = seq.upper()

    # Check for valid sequence
    for aa in seq:
        if aa not in bioinfo_dicts.aa.keys():
            raise RuntimeError(aa + ' is not a valid amino acid.')

    # Count negative residues (Es and Cs)
    return seq.count('D') + seq.count('E')

def find_codon(codon, seq):
    """Find a specified codon with a given sequence."""

    i = 0
    # Scan sequence until we hit the start codon or the end of the sequence
    while seq[i:i+3] != codon and i < len(seq):
        i += 1

    if i == len(seq):
        return -1

    return i

def equilib_conc(Kd, ca0, cb0):
    """Finds the concentrations of all species in a titration
    reaction. Returns a tuple with [AB], [A], [B] respectively"""
    
