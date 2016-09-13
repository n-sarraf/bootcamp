

def gc_blocks(seq, block_size):
    """ Split seq into blocks of specified size and calculate gc value """

    seq_list=[]
    gc_list=[]

    # Split seq in blocks of user-specified size
    for i in range(0, len(seq), block_size):
        if (block_size+i)<=len(seq):
            seq_list.append(seq[i:block_size+i])

    gc_count=0
    gc_value=0

    # Count number of 'G' and 'C' in block and calculate gc value
    for i, base in enumerate(seq_list):
        for i, base in enumerate(seq_list[i]):
            if base in 'Gg':
                gc_count += 1
            elif base in 'Cc':
                gc_count += 1
            else:
                gc_count += 0
        gc_value=gc_count/block_size
        gc_list.append(gc_value)
        gc_count=0

    gc_tuple = tuple(gc_list)
    print(seq_list)
    return gc_tuple


def mapped_seq = gc_map(seq, block_size, gc_thresh):
