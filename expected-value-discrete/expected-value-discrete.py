import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    Raises: ValueError if probabilities are invalid
    """
    x = np.asarray(x, dtype=float)
    p = np.asarray(p, dtype=float)

    if x.shape != p.shape:
        raise ValueError("x and p must have the same shape")

    if np.any(p < 0):
        raise ValueError("Probabilities must be nonnegative")

    if not np.isclose(np.sum(p), 1.0, atol=1e-6):
        raise ValueError("Probabilities must sum to 1")

    return np.dot(x, p)
