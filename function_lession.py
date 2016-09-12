def ratio(x, y):
    """The ratio of 'x' to 'y'."""
    return x / y

def answer_to_the_ultimate_question_of_life_the_universe_and_everything():
    """Simpler program than Deep Throught's, I bet."""
    return 42

def think_too_much():
    """Express Caesar's skepticism about Cassius."""
    print("""Yond Cassius has a lean and hungry look,
    He thinks too much; such men are dangerous.""")

def complement_base(base, material="DNA"):
    """Return the Watson-Crick complement of a base."""
    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == "RNA":
            return 'U'
        else:
            raise RuntimeError('Invalid material.')
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'

def reverse_complement(seq, material="DNA"):
    """Compute reverse complement of a DNA sequence."""
    # Initialize empty string
    rev_comp = ''
    # Run through the entire sequence and put in the reverse sequence
    for base in reversed(seq):
        rev_comp += complement_base(base, material=material)
    return rev_comp
