import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.asarray(x)
    sig = 1/(1+np.exp(-x))
    out = x * sig
    return out
    pass