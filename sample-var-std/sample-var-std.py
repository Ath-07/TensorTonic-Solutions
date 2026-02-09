import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.asarray(x)
    x_mean = np.mean(x)
    n = len(x)
    var = (1/(n-1))*(np.sum((x-x_mean) ** 2))
    std = np.sqrt(var)
    return (var, std)
    pass