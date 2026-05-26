import numpy as np

def relu(x):
    return np.maximum(x, 0)

def bottleneck_block(x, W1, W2, W3, Ws):
    """
    Returns: np.ndarray with bottleneck residual block output (compress, process, expand + skip)
    """
    x = np.asarray(x)
    W1 = np.asarray(W1)
    W2 = np.asarray(W2)
    W3 = np.asarray(W3)
    # YOUR CODE HERE
    if Ws == None:
        shortcut = x
    else:
        Ws = np.asarray(Ws)
        shortcut = x @ Ws

    L1 = relu(x @ W1)
    L2 = relu(L1 @ W2)
    L3 = L2 @ W3

    return relu(L3 + shortcut)
    pass
