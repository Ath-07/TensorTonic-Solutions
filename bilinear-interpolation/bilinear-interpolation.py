def bilinear_resize(image, new_h, new_w):
    """
    Resize a 2D grid using bilinear interpolation.
    """
    # Write code here
    H = len(image)
    W = len(image[0])
    output = []

    if new_h == 1:
        y_scale = 0
    else:
        y_scale = (H - 1) / (new_h - 1)

    if new_w == 1:
        x_scale = 0
    else:
        x_scale = (W - 1) / (new_w - 1)

    for i in range(new_h):
        row = []
        src_y = i * y_scale
        y0 = int(src_y)
        y1 = min(y0 + 1, H - 1)
        dy = src_y - y0

        for j in range(new_w):
            src_x = j * x_scale
            x0 = int(src_x)
            x1 = min(x0 + 1, W - 1)
            dx = src_x - x0

            # Four neighbors
            v00 = image[y0][x0]
            v10 = image[y1][x0]
            v01 = image[y0][x1]
            v11 = image[y1][x1]

            # Bilinear interpolation
            value = (
                v00 * (1 - dy) * (1 - dx) +
                v10 * dy * (1 - dx) +
                v01 * (1 - dy) * dx +
                v11 * dy * dx
            )

            row.append(float(value))

        output.append(row)

    return output
    pass