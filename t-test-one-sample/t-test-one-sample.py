import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    x = np.asarray(x)
    n = len(x)
    mean = np.mean(x)
    std = np.sqrt((1/(n-1))*np.sum((x-mean)**2))
    t_stat = (mean-mu0)/(std/np.sqrt(n))
    return t_stat
    pass