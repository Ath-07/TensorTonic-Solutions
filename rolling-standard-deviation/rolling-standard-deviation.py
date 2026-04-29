def rolling_std(values, window_size):
    """
    Compute the rolling population standard deviation.
    """
    # Write code here
    out = []
    for i in range(len(values) - window_size + 1):
        sum = 0
        for j in range(window_size):
            sum += values[i+j]
        mean = sum / window_size
        sq_sum = 0
        for j in range(window_size):
            sq_sum += (values[i+j] - mean)**2
        std_dev = (sq_sum/window_size) ** 0.5
        out.append(std_dev)

    return out