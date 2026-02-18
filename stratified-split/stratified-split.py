import numpy as np

def stratified_split(X, y, test_size=0.2, rng=None):
    X = np.asarray(X)
    y = np.asarray(y)

    if rng is None:
        rng = np.random.default_rng()

    classes, counts = np.unique(y, return_counts=True)

    train_parts = []
    test_parts = []

    for c, n_c in zip(classes, counts):
        idx = np.where(y == c)[0]
        rng.shuffle(idx)

        # reference rule
        n_test = int(round(n_c * test_size))
        if test_size > 0 and n_c >= 2:
            n_test = max(1, min(n_test, n_c - 1))
        else:
            n_test = 0

        test_parts.append(idx[:n_test])
        train_parts.append(idx[n_test:])

    train_idx = np.concatenate(train_parts)
    test_idx = np.concatenate(test_parts)
    train_idx = np.sort(train_idx)
    test_idx = np.sort(test_idx)

    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]