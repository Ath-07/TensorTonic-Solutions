import numpy as np

def relu(x):
    return np.maximum(x, 0)

def conv_block(x, W1, W2, Ws):
    """
    Returns: np.ndarray with sum of main path output and projected shortcut
    """
    # YOUR CODE HERE
    W1 = np.asarray(W1)
    W2 = np.asarray(W2)
    Ws = np.asarray(Ws)

    s = x @ Ws
    h = relu(x @ W1)
    z = h @ W2
    y = relu(z + s)
    return y
    pass
