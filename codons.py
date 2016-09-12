codon = input('Input your codon: ')
codon_tuple = ('UAA', 'UAG', 'UGA')

if codon == 'AUG':
    print('This codon is the start codon.')
elif codon in codon_tuple:
    print('This is a stop codon.')
else:
    print('This is neither a start nor stop codon.')
