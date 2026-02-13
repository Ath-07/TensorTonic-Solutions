import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.asarray(X)
    axis_max = np.max(X, axis, keepdims=True)
    axis_min = np.min(X, axis, keepdims=True)
    X_scaled = (X-axis_min)/np.maximum(axis_max-axis_min, eps)
    return X_scaled
    pass