import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.asarray(v)
    norm = np.linalg.norm(v, axis=-1, keepdims=True)
    norm = np.where(norm < 1e-10, 1.0, norm)
    return v/norm
    pass 