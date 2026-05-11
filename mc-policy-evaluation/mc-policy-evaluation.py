import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    """
    Returns: V (NumPy array of shape (n_states,))
    """
    # Write code here
    returns_sum = np.zeros(n_states, dtype=float)
    returns_count = np.zeros(n_states, dtype=int)

    for episode in episodes:
        G = 0
        visited = set()
        returns = [0] * len(episode)
        
        for t in reversed(range(len(episode))):
            state, reward = episode[t]
            G = reward + gamma * G
            returns[t] = G

        for t, (state, _) in enumerate(episode):
            if state not in visited:
                visited.add(state)
                returns_sum[state] += returns[t]
                returns_count[state] += 1

    V = np.zeros(n_states, dtype=float)

    for s in range(n_states):
        if returns_count[s] > 0:
            V[s] = returns_sum[s] / returns_count[s]

    return V
    pass
