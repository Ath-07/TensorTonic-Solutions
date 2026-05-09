def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    # Write code here
    n_user = len(matrix)
    n_movies = len(matrix[0])

    for i in range(n_user):
        sum = 0
        count = 0
        for j in range(n_movies):
            if matrix[i][j] != 0:
                sum += matrix[i][j]
                count += 1
        if count == 0:
            continue
        mean = sum / count
        for j in range(n_movies):
            if matrix[i][j] != 0:
                matrix[i][j] -= mean
    return matrix
    