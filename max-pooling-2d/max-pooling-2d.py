def max_pooling_2d(X, pool_size):
    """
    Apply 2D max pooling with non-overlapping windows.
    """
    # Write code here
    h = len(X)
    w = len(X[0])

    h_out = h // pool_size
    w_out = w // pool_size

    p = pool_size

    out = [[0 for _ in range(w_out)] for _ in range(h_out)]

    for i in range(h_out):
        for j in range(w_out):
            maximum = float('-inf')
            for a in range(p):
                for b in range(p):
                    maximum = max(maximum, X[i*p+a][j*p+b])
            out[i][j] = maximum

    return out 