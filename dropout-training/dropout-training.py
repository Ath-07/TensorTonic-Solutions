import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.asarray(x)

    # Choose random generator
    rand = rng.random if rng is not None else np.random.random

    keep_prob = 1.0 - p

    # Generate mask (True = keep)
    mask = rand(x.shape) < keep_prob

    # Create dropout pattern
    dropout_pattern = mask.astype(x.dtype) * (1.0 / keep_prob)

    # Apply element-wise
    output = x * dropout_pattern

    return output, dropout_pattern
    pass