import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """
    # Your code here
    R_z = np.array([
        [np.cos(theta), ((-1)*(np.sin(theta))), 0], 
        [np.sin(theta), np.cos(theta), 0], 
        [0, 0, 1]
    ])
    points = np.asarray(points)
    if points.ndim == 1:
        points.reshape((1,3))
        new = R_z @ points
        return new.reshape((3,))
    else:
        return points @ R_z.T
    pass