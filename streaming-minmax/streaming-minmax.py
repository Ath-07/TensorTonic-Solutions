import numpy as np

def streaming_minmax_init(D):
    """
    Initialize state dict with min, max arrays of shape (D,).
    """
    # Write code here
    min_arr = np.full((D,), +np.inf)
    max_arr = np.full((D,), -np.inf)
    state = {
        'min' : min_arr,
        'max' : max_arr
    }
    return state
    pass

def streaming_minmax_update(state, X_batch, eps=1e-8):
    """
    Update state's min/max with X_batch, return normalized batch.
    """
    # Write code here
    X_batch = np.asarray(X_batch)
    min_batch = X_batch.min(axis=0)
    max_batch = X_batch.max(axis=0)
    state["min"] = np.minimum(state["min"], min_batch)
    state["max"] = np.maximum(state["max"], max_batch)
    denom = state["max"] - state["min"]
    X_norm = (X_batch - state["min"]) / (denom + eps)
    return X_norm
    pass