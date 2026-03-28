import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if not max_len: max_len = max(len(seq) for seq in seqs)
    sq = np.full(shape=(len(seqs), max_len), fill_value=pad_value)
    for i, seq in enumerate(seqs): sq[i, :min(max_len,len(seq))] = seq[ :min(max_len,len(seq))]
    return sq.tolist()

        