

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

    return gc_tuple, seq_list


def gc_map(seq, block_size, gc_thresh):

    gc_tuple, seq_list = gc_blocks(seq, block_size)
    gc_above = []
    map_seq = ''

    for i, base in enumerate(gc_tuple):
        if gc_tuple[i]>gc_thresh:
            gc_above.append(True)
        else:
            gc_above.append(False)

    for i, base in enumerate(seq_list):
        if gc_above[i] == True:
            up = str(seq_list[i]).upper()
            map_seq += up
        else:
            low = str(seq_list[i]).lower()
            map_seq += low

    return map_seq
