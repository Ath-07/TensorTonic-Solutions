def priority_replay_sample(priorities, alpha, beta):
    """
    Compute sampling probabilities and importance sampling weights for PER.
    """
    # Write code here
    powered_priorities = [p**alpha for p in priorities]
    total_pow_prior = 0
    for i in range(len(priorities)):
        total_pow_prior += powered_priorities[i]
    sampling_probabilities = [round(p/total_pow_prior, 6) for p in powered_priorities]
    N = len(priorities)
    weights = [((N*P)**(-beta)) for P in sampling_probabilities]
    max_w = max(weights)
    nor_weights = [w/max_w for w in weights]
    return [sampling_probabilities, nor_weights]