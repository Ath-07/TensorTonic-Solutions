import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.asarray(x)
    neg_x = -1*x
    exp_x = np.exp(x)
    exp_negx = np.exp(neg_x)
    tanh = (exp_x - exp_negx) / (exp_x + exp_negx)
    return tanh
    pass