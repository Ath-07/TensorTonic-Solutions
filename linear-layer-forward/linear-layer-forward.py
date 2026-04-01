def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here
    n = len(X)
    d_in = len(W)
    d_out = len(b)

    Y = [[0 for _ in range(d_out)] for _ in range(n)]

    for i in range(n):
        for j in range(d_out):
            for k in range(d_in):
                Y[i][j] += X[i][k] * W[k][j] 

    for m in range(n):
        for j in range(d_out):
            Y[m][j] += b[j]

    return Y
    