import numpy as np

def epsilon_greedy(q_values, epsilon, rng=None):
    """
    Returns: action index (int)
    """
    # Write code here
    if rng is None:
        rng = np.random.default_rng()

    n_actions = len(q_values)

    if rng.random() < epsilon:
        return int(rng.integers(n_actions))

    return int(np.argmax(q_values))
    
    pass
