import bioinfo_dicts

def one_to_three(seq):
    seq = seq.upper()
    # Build conversions
    aa_list = []
    for acid in seq:
        if acid in bioinfo_dicts.aa.keys():
            aa_list += [bioinfo_dicts.aa[acid], '-']
        else:
            raise RuntimeError(acid + ' is not a valid amino acid')
    return ''.join(aa_list[:-1])

try:
    import gc_content
    have_gc = True
except ImportError as e:
    have_gc = False

seq = 'ACGATCAGCTAGCAGCGCGCGGCTACGAC'

if have_gc:
    print(gc_content.gc(seq))
else:
    print((seq.count('G') + seq.count('C')) / len(seq))
