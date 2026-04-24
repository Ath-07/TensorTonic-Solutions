def sobel_edges(image):
    """
    Apply the Sobel operator to detect edges.
    """
    # Write code here
    H = len(image)
    W = len(image[0])
    result = [[0.0] * W for _ in range(H)]
    
    padded = [[0] * (W + 2) for _ in range(H + 2)]
    for i in range(H):
        for j in range(W):
            padded[i + 1][j + 1] = image[i][j]
    
    Kx = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]
    
    Ky = [
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ]
    
    # Step 2–4: Convolution + magnitude
    for i in range(H):
        for j in range(W):
            Gx = 0
            Gy = 0
            
            for x in range(3):
                for y in range(3):
                    val = padded[i + x][j + y]
                    Gx += val * Kx[x][y]
                    Gy += val * Ky[x][y]
            
            result[i][j] = math.sqrt(Gx**2 + Gy**2)
    
    return result