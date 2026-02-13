import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.asarray(X)
    axis_mean = np.mean(X, axis, keepdims=True)
    axis_dev = np.std(X, axis, keepdims=True, dtype = np.float32)
    X_standardize = (X-axis_mean)/(axis_dev+eps)
    return X_standardize
    pass