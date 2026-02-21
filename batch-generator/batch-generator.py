import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    """
    Randomly shuffle a dataset and yield mini-batches (X_batch, y_batch).
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)

    if batch_size <= 0:
        return None

    if len(X) != len(y):
        return None

    if rng is None:
        rng = np.random.default_rng()
    
    N = len(X)
    indices = rng.permutation(N)

    X_shuffled = X[indices]
    y_shuffled = y[indices]
   
    for start in range(0, N, batch_size):
        end = start + batch_size

        if end > N and drop_last:
            break

        yield X_shuffled[start:end], y_shuffled[start:end]
    pass