def item_cf_predict(user_ratings, item_similarities, target):
    """
    Predict the rating using item-based collaborative filtering.
    """
    # Write code here
    numerator = 0
    denominator = 0
    for i in range(len(user_ratings)):
        if i == target or user_ratings[i] == 0 or item_similarities[i] < 0:
            continue
        else:
            numerator += user_ratings[i] * item_similarities[i]
            denominator += item_similarities[i]

    if denominator == 0:
        return 0.0

    return numerator/denominator