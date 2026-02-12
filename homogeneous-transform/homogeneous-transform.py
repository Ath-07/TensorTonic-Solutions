import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here
    points = np.asarray(points)
    Flag = False
    if points.ndim == 1:
        points = points.reshape(1, -1)
        Flag = True
    ones_col = np.ones((points.shape[0], 1))
    p_h = np.hstack((points, ones_col))
    p_trans = (T @ p_h.T).T
    out = p_trans[:, :3]
    if Flag == True:
        out = out.reshape(3,)
    return out
    pass