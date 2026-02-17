import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    matrix = np.asarray(matrix)
    if axis is not None:
        if not isinstance(axis, int):
            return None
        if axis < -matrix.ndim or axis >= matrix.ndim:
            return None
        if matrix.ndim == 1 and axis not in (0, -1):
            return None
        if matrix.ndim != 2:
            return None

    if norm_type == "l2":
        norm = np.sqrt(np.sum(matrix**2, axis=axis, keepdims=True))
        norm[norm == 0] = 1.0
        matrix_nor = matrix/norm
    elif norm_type == "l1":
        norm = np.sum(np.abs(matrix), axis=axis, keepdims=True)
        norm[norm == 0] = 1.0
        matrix_nor = matrix/norm 
    elif norm_type == "max":
        norm = np.max(np.abs(matrix), axis=axis, keepdims=True)
        norm[norm == 0] = 1.0
        matrix_nor = matrix/norm
    else:
        return None
    return matrix_nor
    pass