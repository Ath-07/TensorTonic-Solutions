import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if max_len == None:
        max_len = max(len(seq) for seq in seqs)

    N = len(seqs)
    L = max_len

    out = np.full((N, L), pad_value)

    for i in range(N):
        for j in range(L):
            if i < N and j < len(seqs[i]):
                out[i, j] = seqs[i][j]
    return out
    pass