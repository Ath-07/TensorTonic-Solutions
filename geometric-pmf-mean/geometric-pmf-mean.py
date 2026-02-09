import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    mean = 1.0/p
    k = np.asarray(k)
    pmf = np.array([(((1-p)**(i-1)) * p) for i in k], dtype = np.float64)
    pmf.astype(np.float64)
    return (pmf, mean)
    pass