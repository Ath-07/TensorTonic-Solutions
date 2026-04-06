import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    # Write code here
    if not isinstance(x, np.ndarray):
        raise ValueError("Input must be a NumPy array")
    
    if x.ndim == 3:
        # Shape: (C, H, W) → (C,)
        return np.mean(x, axis=(1, 2), dtype=np.float64)
    
    elif x.ndim == 4:
        # Shape: (N, C, H, W) → (N, C)
        return np.mean(x, axis=(2, 3), dtype=np.float64)
    
    else:
        raise ValueError("Input must have shape (C,H,W) or (N,C,H,W)")
    pass