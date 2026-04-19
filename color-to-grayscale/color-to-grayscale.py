def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    rows = len(image)
    columns = len(image[0])

    out = []

    for i in range(rows):
        out_r = []
        for j in range(columns):
            gray_val = (0.299*image[i][j][0]) + (0.587*image[i][j][1]) + (0.114*image[i][j][2])
            out_r.append(gray_val)

        out.append(out_r)

    return out