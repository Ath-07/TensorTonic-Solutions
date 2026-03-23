import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    # Write code here
    anchor = np.asarray(anchor)
    positive = np.asarray(positive)
    negative = np.asarray(negative)

    dap = np.sum((anchor - positive)**2, axis=-1)
    dan = np.sum((anchor - negative)**2, axis=-1)

    loss = np.maximum(0, dap-dan+margin)
    return np.mean(loss)
    pass