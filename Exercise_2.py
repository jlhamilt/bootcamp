# Bootcamp 9/12/2016 Example exercises

# Import for translating a sequence
import bioinfo_dicts

# Exercise 2.2: Parsing the SPI1 Genome
# Only need to run it once
# with open('data/salmonella_spi1_region.fna', 'r') as f, \
# open('spi1_region.txt', 'w') as f_out:
#
#      # Get all the lines
#      lines = f.readlines()
#
#      # Ignore first line and write the combined sequence to f_out
#      for line in lines:
#          if line[0] != '>':
#              f_out.write(line.rstrip())


# Exercise 2.3: Pathogenicity islands
def gc_blocks(seq, block_size):
    """Breaks a given sequence into blocks, then computes the GC content."""

    # Make all capital
    seq = seq.upper()
    iterations = len(seq) // block_size

    # Iterate through finding the GC content
    gc = []
    for i in range(iterations):
        block = seq[i*block_size:(i+1)*block_size]
        gc.append((block.count('G') + block.count('C')) / block_size)
    return tuple(gc)


def gc_map(seq, block_size, gc_thresh):
    """Returns a sequence with every block in the sequence having a GC
    content above the threshold as capital and below as lowercase."""

    # Get the GC content for each block
    gc_cont = gc_blocks(seq, block_size)

    # Iterate through the sequence adding the appropriate cased block_size
    new_seq = ''
    iterations = len(seq) // block_size
    for i in range(iterations):
        block = seq[i*block_size:(i+1)*block_size]
        if gc_cont[i] >= gc_thresh:
            new_seq += block.upper()
        else:
            new_seq += block.lower()
    return new_seq


# Write a GC-mapped sequence fo the SPI1 region to a new FASTA file
with open('data/salmonella_spi1_region.fna', 'r') as orig_seq, \
open('spi1_region.txt', 'r') as seq, \
open('data/salmonella_spi1_region_mapped.fna', 'w') as new_seq:

    # Make the header for the new file
    header = orig_seq.readline()
    new_seq.write(header)

    # Write the mapped sequence with 60 characters per line
    i = 0
    seq = seq.read()
    seq_mapped = gc_map(seq, 1000, 0.45)
    while i < len(seq):
        new_seq.write(seq_mapped[i:i+60] + '\n')
        i += 60


# Exercise 2.4: ORF detection
def seq_positions(seq, codon):
    """Finds all positions in the sequence with the given codon."""

    positions = []
    i = 0
    while codon in seq[i:]:
        pos = seq.find(codon, i)
        positions.append(pos)
        i = pos + 1
    return positions


def longest_orf(seq):
    """Returns the longest open read frame in the sequence."""

    # Find possible start positions
    starts = seq_positions(seq, 'ATG')

    # Find possible end positions
    ends = seq_positions(seq, 'TGA') + seq_positions(seq, 'TAG') + seq_positions(seq, 'TAA')

    # Go through all starts and ends keeping track of longest orf
    orf = ''
    for start in starts:
        for end in ends:
            if start < end and (end - start) % 3 == 0 and len(orf) < (end - start):
                orf = seq[start:end+3]

    return orf

def dna_to_protein(seq):
    """Converts a given sequence to a protein sequence."""

    # Verify a convertible sequence
    if len(seq) % 3 != 0:
        raise RuntimeError('Total number of bases must be a multiple of 3')

    # Iterate through adding the proteins
    protein = ''
    for i in range(0, len(seq), 3):
        protein += bioinfo_dicts.codons[seq[i:i+3]]
    return protein


# Create a protein sequence of the longest ORF in the SPI1 region
# Has a long runtime so comment out if not needed
# with open('salmonella_spi1_region_protein.fna', 'w') as pro:
#     orf = longest_orf(seq)
#     pro.write(dna_to_protein(orf))
