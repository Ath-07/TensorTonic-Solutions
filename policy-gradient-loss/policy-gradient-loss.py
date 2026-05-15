def policy_gradient_loss(log_probs, rewards, gamma):
    """
    Compute REINFORCE policy gradient loss with mean-return baseline.
    """
    # Write code here
    T = len(rewards)

    returns = [0.0] * T
    G = 0.0

    for t in reversed(range(T)):
        G = rewards[t] + gamma * G
        returns[t] = G

    mean_return = sum(returns) / T
    advantages = [g - mean_return for g in returns]

    loss = -sum(lp * adv for lp, adv in zip(log_probs, advantages)) / T
    return loss