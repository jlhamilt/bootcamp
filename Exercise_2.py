# Bootcamp 9/12/2016 Example exercises

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
