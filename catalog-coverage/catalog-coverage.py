def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here
    n_user = len(recommendations)
    unique = set()
    for i in range(n_user):
        unique.update(recommendations[i])

    n_unique = len(unique)
    return n_unique / n_items