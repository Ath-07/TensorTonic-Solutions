import numpy as np

def batch_norm_block(x, W1, W2, gamma1, beta1, gamma2, beta2, mode):
    """
    Returns: np.ndarray of same shape as input with batch-normalized and skip-connected output
    """
    # YOUR CODE HERE
    eps = 1e-5
    x = np.asarray(x)
    W1 = np.asarray(W1)
    W2 = np.asarray(W2)

    def batch_norm(z, gamma, beta):
        mean = z.mean(axis=0)
        var = z.var(axis=0)

        z_hat = (z - mean) / np.sqrt(var + eps)

        return gamma * z_hat + beta

    def relu(z):
        return np.maximum(0, z)

    if mode == "post":
        # Conv -> BN -> ReLU
        out = x @ W1
        out = batch_norm(out, gamma1, beta1)
        out = relu(out)

        # Conv -> BN
        out = out @ W2
        out = batch_norm(out, gamma2, beta2)

        # Add skip connection -> ReLU
        out = out + x
        out = relu(out)

    elif mode == "pre":
        # BN -> ReLU -> Conv
        out = batch_norm(x, gamma1, beta1)
        out = relu(out)
        out = out @ W1

        # BN -> ReLU -> Conv
        out = batch_norm(out, gamma2, beta2)
        out = relu(out)
        out = out @ W2

        # Add skip connection
        out = out + x

    else:
        raise ValueError("mode must be 'post' or 'pre'")

    # Round to 4 decimal places
    out = np.round(out, 4)

    return {
        "output": out.tolist(),
        "mode": mode
    }
    pass
