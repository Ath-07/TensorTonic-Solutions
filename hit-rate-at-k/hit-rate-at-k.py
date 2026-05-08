def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    n_users = len(recommendations)
    hit_count = 0
    for i in range(n_users):
        rec = set(recommendations[i][:k])
        gt = set(ground_truth[i])

        inter = rec & gt
        if len(inter) != 0:
            hit_count += 1

    return hit_count/n_users
        