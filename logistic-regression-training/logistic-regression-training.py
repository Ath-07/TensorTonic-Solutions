import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    data_points, features = X.shape
    w = np.zeros(features)
    b = 0.0

    for i in range(steps):
        p = _sigmoid((X @ w) + b)
        dw = X.T @ (p - y) / data_points
        db = np.mean(p - y)
        w = w - lr * dw
        b = b - lr * db

    return w, b
    pass