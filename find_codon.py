

def find_codon_lesson6(codon, seq):
    """Find a specified codon with a given sequence."""

    for b in codon:
        if b not in 'AaTtGgUuCc':
            raise RuntimeError(b + ' is not a valid base.')

    # Convert codon to uppercase
    codon = codon.upper()

    # Initialize counter
    i = 0

    # Scan sequence until we hit the start codon or the end of the sequence
    while seq[i:i+3] != codon and i < len(seq):
        i += 1

    if i == len(seq):
        return -1
    else:
        return i
