import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    v = np.asarray(v)
    w = np.asarray(w)
    v_norm = np.linalg.norm(v)
    w_norm = np.linalg.norm(w)
    if v_norm < 10e-10 or w_norm < 10e-10:
        return np.nan
    else:
        dot_pro = v @ w
        cos_theta = np.clip(dot_pro / (v_norm * w_norm), -1, 1)
        return np.arccos(cos_theta)
    pass