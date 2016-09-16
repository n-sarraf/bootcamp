
import bioinfo_dicts

def one_to_three(seq):
    """ Convert single-letter amino acid code to three-letter. """

    seq = seq.upper()

    # Build conversion
    aa_list = []
    for amino_acid in seq:
        if amino_acid in bioinfo_dicts.aa.keys():
            aa_list += [bioinfo_dicts.aa[amino_acid], '-']
        else:
            raise RuntimeError(amino_acid + ' is not a valid amino acid.')

    return ''.join(aa_list[:-1])


try:
    import gc_content
    have_gc = True
except ImportError as e:
    have_gc = False

seq = 'ACGATCAGTCATCTA'

if have_gc:
    print(gc_content.gc(seq))
else:
    print((seq.count('G') + seq.count('C')) / len(seq))
