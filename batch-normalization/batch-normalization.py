import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x = np.asarray(x)
    gamma = np.asarray(gamma)
    beta = np.asarray(beta)
    
    if x.ndim == 2:
        # Case 1: (N, D)
        mean = np.mean(x, axis=0, keepdims=True)
        var = np.var(x, axis=0, keepdims=True)
        
        x_hat = (x - mean) / np.sqrt(var + eps)
        
        # gamma and beta shape: (D,) → broadcast automatically
        out = gamma * x_hat + beta

    elif x.ndim == 4:
        # Case 2: (N, C, H, W)
        mean = np.mean(x, axis=(0, 2, 3), keepdims=True)
        var = np.var(x, axis=(0, 2, 3), keepdims=True)
        
        x_hat = (x - mean) / np.sqrt(var + eps)
        
        # reshape gamma, beta to (1, C, 1, 1)
        gamma = gamma.reshape(1, -1, 1, 1)
        beta = beta.reshape(1, -1, 1, 1)
        
        out = gamma * x_hat + beta

    return out 
    pass