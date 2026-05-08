def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    out = []
    for (avg_rating, num_votes) in items:
        WR = ((num_votes/(num_votes + min_votes)) * avg_rating) + ((min_votes/(num_votes + min_votes)) * global_mean)
        out.append(WR)

    return out