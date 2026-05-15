import numpy as np

def compute_advantage(states, rewards, V, gamma):
    """
    Returns: A (NumPy array of advantages)
    """
    # Write code here
    n = len(rewards)

    returns = np.zeros(n, dtype=float)

    G = 0.0
    for t in reversed(range(n)):
        G = rewards[t] + gamma * G
        returns[t] = G

    # Compute advantages
    advantages = np.zeros(n, dtype=float)
    for t in range(n):
        advantages[t] = returns[t] - V[states[t]]

    return advantages
    pass
