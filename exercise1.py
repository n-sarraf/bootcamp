
def complement_base(base, material='DNA'):
    """Return the Watson-Crick complement of a base."""

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'


def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of a nucleic acid sequence."""

    # Initialize empty string
    rev_comp = ''
    comp = ''

    # Loop through and add new rev comp bases
    for base in seq:
        comp += complement_base(base, material=material)

    for i in range(len(comp)):
        rev_comp += comp[len(comp)-(i+1)]

    return rev_comp

def loopless_reverse_complement(seq, material='DNA'):
    """Compute reverse complement of a nucleic acid sequence without using a for loop."""

    # Initialize empty string
    rev_seq = ''
    rev_comp = ''

    rev_seq = seq[::-1]

    rev_seq = rev_seq.replace('G','c')
    rev_seq = rev_seq.replace('C','g')
    rev_seq = rev_seq.replace('T','a')

    if material=='DNA':
        rev_seq = rev_seq.replace('A','t')
    elif material=='RNA':
        rev_seq = rev_seq.replace('A','u')

    rev_comp = rev_seq.upper()

    return rev_comp
