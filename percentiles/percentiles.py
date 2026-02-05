import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.asarray(x)
    q = np.asarray(q)
    r = []
    for i in q:
        r.append(np.percentile(x, i, method='linear'))
    return np.asarray(r)
    pass