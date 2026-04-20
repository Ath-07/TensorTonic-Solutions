def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    out = [0 for _ in range(256)]
    r = len(image)
    c = len(image[0])
    for i in range(r):
        for j in range(c):
            out[image[i][j]] += 1

    return out