import numpy as np

def layer_norm(x: np.ndarray, gamma: np.ndarray, beta: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    """
    Returns: Normalized array of same shape as x
    """
    # Your code here
    mean_x = np.mean(x, axis=-1, keepdims=True)
    var_x = np.var(x, axis=-1, keepdims=True) 
    out = (gamma * ((x-mean_x)/np.sqrt(var_x+eps))) + beta
    return out
    pass