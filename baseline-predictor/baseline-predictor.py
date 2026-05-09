def baseline_predict(ratings_matrix, target_pairs):
    """
    Compute baseline predictions using global mean and user/item biases.
    """
    # Write code here
    rows = len(ratings_matrix)
    cols = len(ratings_matrix[0])

    ratings = []
    for row in ratings_matrix:
        for val in row:
            if val != 0:
                ratings.append(val)

    mu = sum(ratings) / len(ratings)

    user_bias = []
    for r in range(rows):
        vals = [ratings_matrix[r][c] for c in range(cols) if ratings_matrix[r][c] != 0]
        avg = sum(vals) / len(vals)
        user_bias.append(avg - mu)

    item_bias = []
    for c in range(cols):
        vals = [ratings_matrix[r][c] for r in range(rows) if ratings_matrix[r][c] != 0]
        avg = sum(vals) / len(vals)
        item_bias.append(avg - mu)

    result = []
    for u, i in target_pairs:
        pred = mu + user_bias[u] + item_bias[i]
        result.append(pred)

    return result