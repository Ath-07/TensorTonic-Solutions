def user_based_cf_prediction(similarities, ratings):
    """
    Predict a rating using user-based collaborative filtering.
    """
    # Write code here
    numerator = 0
    denominator = 0
    for i in range(len(similarities)):
        if similarities[i] > 0:
            numerator += similarities[i] * ratings[i]
            denominator += similarities[i]

    if denominator == 0:
        return 0.0

    return numerator/denominator