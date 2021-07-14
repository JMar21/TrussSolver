def make_pairs(seq):
    length = len(seq)
    return[(seq[i], seq[(i+1) % length])
           for i in range(length)
           ]