# Exercise 1.3
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

def reverse_complement_1(seq, material="DNA"):
    """Compute reverse complement of a DNA sequence.
    Doesn't use the reverse function."""
    # Initialize empty string
    rev_comp = ''
    # Run through the entire sequence and put in the reverse sequence
    for base in seq[::-1]:
        rev_comp += complement_base(base, material=material)
    return rev_comp

def reverse_complement_2(seq, material="DNA"):
    """Compute reverse complement of a DNA sequence.
    Uses a while loop rather than a for loop."""
    i = 0
    comp = ''
    while i < len(seq):
        comp += complement_base(seq[i], material=material)
        i += 1
    rev_comp = comp[::-1]
    return rev_comp

def reverse_complement_3(seq, material='DNA'):
    """Compute reverse complement of a DNA sequence without loops."""
    seq = seq.upper()
    # Replacement for each base into lowercase
    comp = seq.replace('T', 'a')
    comp = comp.replace('G', 'c')
    comp = comp.replace('C', 'g')
    # Special replacement for A
    if material == 'DNA':
        comp = comp.replace('A', 't')
    elif material == 'RNA':
        comp = comp.replace('A', 'u')
    else:
        raise RuntimeError('Invalid material')
    rev_comp = comp[::-1].upper()
    return rev_comp




# Exercise 1.4
def longest_substring(str1, str2):
    """Finds the longest common substring between two given strings."""
    # Make string1 the smaller string
    if len(str1) <= len(str2):
        string1 = str1
        string2 = str2
    else:
        string1 = str2
        string2 = str1
    l = len(string1)
    # Iterate through all possible substrings of the smaller string
    for i in range(l):
        for j in range(i):
            # Check if increasingly smaller substrings are in the larger string
            if string1[j:(l-i+j+1)] in string2:
                return(string1[j:(l-i+j+1)])




# Exercise 1.5
def valid_parentheses(seq):
    """"Verifies an equal number of open and closed parentheses."""
    return seq.count('(') == seq.count('(')

def dotparen_to_bp(seq):
    """"Converts dot-parens notation to a tuple of 2-tuples."""
    paren_list = []
    paren_pairs = []
    for i, char in enumerate(seq):
        if char == '(':
            paren_list.append(i)
        elif char == ')':
            paren_pairs.append((paren_list.pop(), i))
    return tuple(paren_pairs)

def valid_hairpin(seq):
    """Verifies if a bp tuple satisfies the hairpin requrement.
    Hairpins can have no less than three bases in a loop."""
    bp = dotparen_to_bp(seq)
    for _, pair in enumerate(bp):
        if (pair[1] - pair[0]) < 4:
            return False
    else:
        return True

def base_match(base1, base2, wobble=True):
    """Checks if two base pairs match."""
    if base1 in 'Gg':
        if wobble:
            return base2 in 'CcUu'
        else:
            return base2 in 'Cc'
    if base1 in 'Cc':
        return base2 in 'Gg'
    if base1 in 'Aa':
        return base2 in 'Uu'
    if base1 in 'Uu' and wobble:
        return base2 in 'AaGg'
    elif base1 in 'Uu':
        return base2 in 'Aa'

def rna_ss_validator(seq, seq_struc, wobble=True):
    """Validates that the given sequence actually forms a hairpin.
    Wobble allows for G to be paired with U in addition to C."""
    # Verify the structure
    if not valid_parentheses(seq_struc):
        print('Not a valid number of parenthesis')
        return 1!=1
    if not valid_hairpin(seq_struc):
        print('Not a valid hairpin structure')
        return 1!=1
    # Create the base pair tuple
    bp = dotparen_to_bp(seq_struc)
    # Give error if base pairs don't match
    err_msg = 'Base index {b1} and base index {b2} do not connect'
    for _, i in enumerate(bp):
        if not base_match(seq[i[0]], seq[i[1]], wobble=wobble):
            print(err_msg.format(b1=str(i[0]), b2=str(i[1])))
            return 1!=1
    else:
        return 1==1
