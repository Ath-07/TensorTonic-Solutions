import numpy as np

def silhouette_score(X, labels):
    """
    Compute the mean Silhouette Score for given points and cluster labels.
    X: np.ndarray of shape (n_samples, n_features)
    labels: np.ndarray of shape (n_samples,)
    Returns: float
    """
    # Write code here
    X = np.asarray(X)
    labels = np.asarray(labels)
    n = len(X)

    diff = X[:, None, :] - X[None, :, :]
    D = np.sqrt(np.sum(diff**2, axis=2))

    unique_labels = np.unique(labels)

    same_cluster = labels[:, None] == labels[None, :]
    np.fill_diagonal(same_cluster, False)

    a = np.sum(D * same_cluster, axis=1) / np.sum(same_cluster, axis=1)
    b = np.full(n, np.inf)

    for lab in unique_labels:
        mask = labels == lab
        dist = np.sum(D[:, mask], axis=1) / np.sum(mask)
        b = np.minimum(b, np.where(labels != lab, dist, np.inf))

    s = (b - a) / np.maximum(a, b)

    return np.mean(s)
    pass