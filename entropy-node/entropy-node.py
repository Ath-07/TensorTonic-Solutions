import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y = np.asarray(y)
    n = len(y)
    eps = 1e-12
    val, counts = np.unique(y, return_counts=True)
    probs = [(c/n) for c in counts]
    probs = np.asarray(probs)
    ready_probs = np.where(probs == 0.0, eps, probs)
    entropy = 0
    for i in range(len(val)):
        if ready_probs[i] == eps:
            continue
        else:
            entropy -= ready_probs[i] * np.log2(ready_probs[i])
    return float(entropy)
    pass