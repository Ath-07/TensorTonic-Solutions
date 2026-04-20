def histogram_equalize(image):
    """
    Apply histogram equalization to enhance image contrast.
    """
    # Write code here
    # Flatten image to compute histogram
    flat = [pixel for row in image for pixel in row]
    total_pixels = len(flat)
    
    # Step 1: Histogram (256 bins)
    hist = [0] * 256
    for pixel in flat:
        hist[pixel] += 1
    
    # Step 2: Compute CDF
    cdf = [0] * 256
    cdf[0] = hist[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + hist[i]
    
    # Step 3: Find cdf_min (first non-zero value)
    cdf_min = 0
    for val in cdf:
        if val > 0:
            cdf_min = val
            break
    
    # Edge case: all pixels same
    if cdf_min == total_pixels:
        return [[0 for _ in row] for row in image]
    
    # Step 4: Create mapping
    mapping = [0] * 256
    for v in range(256):
        mapping[v] = round((cdf[v] - cdf_min) / (total_pixels - cdf_min) * 255)
    
    # Step 5: Apply mapping
    result = []
    for row in image:
        result.append([mapping[pixel] for pixel in row])
    
    return result