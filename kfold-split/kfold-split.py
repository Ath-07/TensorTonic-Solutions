import numpy as np

def kfold_split(N, k, shuffle=True, rng=None):
    """
    Returns: list of length k with tuples (train_idx, val_idx)
    """
    # Write code here
    if k < 2 or k > N:
        return None

    indices = np.arange(N)
    if shuffle:
        if rng is not None:
            indices = rng.permutation(indices)
        else:
            np.random.shuffle(indices)

    folds = np.array_split(indices, k)
    splits = []
    for i in range(k):
        val_idx = folds[i]
        train_idx = np.concatenate(folds[:i] + folds[i+1:]) if k > 1 else np.array([], dtype=int)

        splits.append((train_idx.astype(int), val_idx.astype(int)))

    return splits
    pass
