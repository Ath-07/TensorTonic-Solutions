import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)
    t1 = np.linalg.inv(X.T @ X)
    w = t1 @ X.T @ y
    return w
    pass