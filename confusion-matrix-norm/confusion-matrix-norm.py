import numpy as np

def confusion_matrix_norm(y_true, y_pred, num_classes=None, normalize='none'):
    """
    Compute confusion matrix with optional normalization.
    """
    # Write code here
    eps = 1e-12
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    if y_true.size == 0:
        K = num_classes if num_classes is not None else 0
        return np.zeros((K, K), dtype=float if normalize != "none" else int)

    if num_classes is None:
        K = int(max(y_true.max(), y_pred.max()) + 1)
    else:
        K = int(num_classes)

    if (y_true.min() < 0 or y_pred.min() < 0 or
        y_true.max() >= K or y_pred.max() >= K):
        raise ValueError("Labels must be in [0, K-1]")

    idx = y_true * K + y_pred
    cm = np.bincount(idx, minlength=K * K).reshape(K, K)

    if normalize == "none":
        return cm.astype(np.int64)

    cm = cm.astype(np.float64)

    if normalize == "true":
        # Row-wise normalization
        row_sum = cm.sum(axis=1, keepdims=True)
        row_sum = np.where(row_sum == 0, 1.0, row_sum)
        cm = cm / (row_sum + eps)
        return cm

    elif normalize == "pred":
        # Column-wise normalization
        col_sum = cm.sum(axis=0, keepdims=True)
        col_sum = np.where(col_sum == 0, 1.0, col_sum)
        cm = cm / (col_sum + eps)
        return cm

    elif normalize == "all":
        total = cm.sum()
        total = total if total > 0 else 1.0
        cm = cm / (total + eps)
        return cm

    else:
        raise ValueError("normalize must be one of: 'none', 'true', 'pred', 'all'")
    pass