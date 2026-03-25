import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean") -> float:
    """
    a, b: arrays of shape (N, D) or (D,)  (will broadcast to (N,D))
    y:    array of shape (N,) with values in {0,1}; 1=similar, 0=dissimilar
    margin: float > 0
    reduction: "mean" (default) or "sum"
    Return: float
    """
    # Write code here
    a = np.asarray(a)
    b = np.asarray(b)
    y = np.asarray(y)
    n = len(y)
    if a.ndim == 1:
        a = np.broadcast_to(a, (n, a.shape[0]))
    if b.ndim == 1:
        b = np.broadcast_to(b, (n, b.shape[0]))

    d = np.linalg.norm(a-b, axis=1)
    loss_each = y * d**2 + (1-y) * np.maximum(0, margin-d)**2

    if reduction == "mean":
        return np.mean(loss_each)
    elif reduction == "sum":
        return np.sum(loss_each)
    else:
        return ValueError
    pass