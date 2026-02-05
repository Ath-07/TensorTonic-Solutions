import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x)
    mean = np.mean(x).astype(np.float64)
    median = np.median(x).astype(np.float64)
    counts = Counter(x)
    mode = float(counts.most_common(1)[0][0])
    return (mean, median, mode)
    pass