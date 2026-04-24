def morphological_op(image, kernel, operation):
    """
    Apply morphological erosion or dilation to a binary image.
    """
    # Write code here
    H, W = len(image), len(image[0])
    kH, kW = len(kernel), len(kernel[0])
    
    pad_h, pad_w = kH // 2, kW // 2
    
    padded = [[0] * (W + 2 * pad_w) for _ in range(H + 2 * pad_h)]
    for i in range(H):
        for j in range(W):
            padded[i + pad_h][j + pad_w] = image[i][j]
    
    result = [[0] * W for _ in range(H)]
    
    for i in range(H):
        for j in range(W):
            
            if operation == "erode":
                value = 1  
                
                for x in range(kH):
                    for y in range(kW):
                        if kernel[x][y] == 1:
                            if padded[i + x][j + y] != 1:
                                value = 0
                                break
                    if value == 0:
                        break
                
                result[i][j] = value
            
            elif operation == "dilate":
                value = 0 
                
                for x in range(kH):
                    for y in range(kW):
                        if kernel[x][y] == 1:
                            if padded[i + x][j + y] == 1:
                                value = 1
                                break
                    if value == 1:
                        break
                
                result[i][j] = value
    
    return result