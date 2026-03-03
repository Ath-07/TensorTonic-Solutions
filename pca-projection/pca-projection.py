import numpy as np

def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """
    # Write code here
    X = np.asarray(X)
    n, d = X.shape
    X_mean = np.mean(X, axis=0, keepdims=True)
    X_centered = X - X_mean
    C = (1/(n-1)) * (X_centered.T @ X_centered)
    eigenvalues, eigenvectors = np.linalg.eig(C)
    sorted_val = np.argsort(eigenvalues)[::-1]
    top_k_val = sorted_val[:k]
    top_k_vec = [eigenvectors[:, i] for i in top_k_val]
    X_proj = X_centered @ np.array(top_k_vec).T
    return X_proj