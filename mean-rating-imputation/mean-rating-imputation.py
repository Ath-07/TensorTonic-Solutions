def mean_rating_imputation(ratings_matrix, mode):
    """
    Fill missing ratings (zeros) with user or item means.
    """
    # Write code here
    rows = len(ratings_matrix)
    cols = len(ratings_matrix[0])

    result = [row[:] for row in ratings_matrix]

    if mode == "user":
        for i in range(rows):            
            non_zero = [x for x in ratings_matrix[i] if x != 0]
            mean = sum(non_zero) / len(non_zero) if non_zero else 0

            for j in range(cols):
                if result[i][j] == 0:
                    result[i][j] = mean

    elif mode == "item":
        for j in range(cols):
            non_zero = [ratings_matrix[i][j] for i in range(rows) if ratings_matrix[i][j] != 0]
            mean = sum(non_zero) / len(non_zero) if non_zero else 0

            for i in range(rows):
                if result[i][j] == 0:
                    result[i][j] = mean

    return result