def discount_returns(rewards, gamma):
    """
    Compute the discounted return at every timestep.
    """
    # Write code here
    G = [0 for _ in range(len(rewards))]
    G[len(rewards)-1] = rewards[-1]
    for i in range(len(rewards)-2, -1, -1):
        G[i] = rewards[i] + gamma*G[i+1]
    return G