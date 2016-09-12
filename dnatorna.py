"""
Convert DNA sequences to RNA.
"""

def rna(seq):
    """Convert a DNA sequence to RNA."""
    # Convert to uppercase then change T to U
    seq = seq.upper()
    return seq.replace('T', 'U')
