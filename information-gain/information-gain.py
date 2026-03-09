import numpy as np

def _entropy(y):
    """
    Helper: Compute Shannon entropy (base 2) for labels y.
    """
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    vals, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) if p.size else 0.0

def information_gain(y, split_mask):
    """
    Compute Information Gain of a binary split on labels y.
    Use the _entropy() helper above.
    """
    # Write code here
    y = np.asarray(y)
    split_mask = np.asarray(split_mask)
    h_y = _entropy(y)
    left_idx = np.where(split_mask == True)
    right_idx = np.where(split_mask == False)
    left_split = y[left_idx]
    right_split = y[right_idx]
    n_l = len(left_split)
    n_r = len(right_split)
    n = n_l + n_r
    h_yl = _entropy(left_split)
    h_yr = _entropy(right_split)
    IG = h_y - (((n_l/n)*h_yl) + ((n_r/n)*h_yr))
    return IG
    pass
