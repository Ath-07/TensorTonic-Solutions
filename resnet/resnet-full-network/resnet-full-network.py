import numpy as np

def relu(x):
    return np.maximum(0, x)

def resnet_forward(x, conv1, W1_b1, W2_b1, W1_b2, W2_b2, Ws_b2, fc):
    """
    Returns: np.ndarray of shape (batch, num_classes) with classification logits
    """
    # YOUR CODE HERE
    x = np.asarray(x)
    conv1 = np.asarray(conv1)
    

    # Initial "conv1" + ReLU
    out = relu(x @ conv1)

    # ----- Residual Block 1 (identity shortcut) -----
    identity = out
    residual = relu(out @ W1_b1)
    residual = residual @ W2_b1
    out = relu(residual + identity)

    # ----- Residual Block 2 (projection shortcut) -----
    identity = out @ Ws_b2
    residual = relu(out @ W1_b2)
    residual = residual @ W2_b2
    out = relu(residual + identity)

    # Final fully connected layer (logits)
    logits = out @ fc

    return logits
    pass
