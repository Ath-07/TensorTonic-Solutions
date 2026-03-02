import numpy as np

def knn_distance(X_train, X_test, k):
    """
    Compute pairwise distances and return k nearest neighbor indices.
    """
    # Write code here
    X_train = np.asarray(X_train)
    X_test = np.asarray(X_test)

    if X_train.ndim == 1:
        X_train = X_train.reshape(-1, 1)
    if X_test.ndim == 1:
        X_test = X_test.reshape(-1, 1)

    distance = X_test[:, np.newaxis, :] - X_train[np.newaxis, :, :]
    dist = np.sqrt(np.sum(distance**2, axis=2))
    sorted_idx = np.argsort(dist, axis = 1)

    n_train = X_train.shape[0]
    n_test = X_test.shape[0]

    actual_k = min(k, n_train)
    result = sorted_idx[:, :actual_k]

    if k > n_train:
        padding = -1 * np.ones((n_test, k - n_train), dtype=int)
        result = np.hstack((result, padding))
    return result
    pass