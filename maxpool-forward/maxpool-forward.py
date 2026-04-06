def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    # Write code here
    H = len(X)
    W = len(X[0])
    p = pool_size
    s = stride
    
    H_out = int((H-p)/s) + 1
    W_out = int((W-p)/s) + 1

    out = [[0 for _ in range(W_out)] for _ in range(H_out)]

    for i in range(H_out):
        for j in range(W_out):
            max_val = float('-inf')
            for a in range(p):
                for b in range(p):
                    val = X[i*s+a][j*s+b]
                    if val > max_val:
                        max_val = val

            out[i][j] = max_val

    return out
    