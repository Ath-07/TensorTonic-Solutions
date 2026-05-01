def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    n = len(values)
    result = []

    for i in range(n - window_size + 1):
        window = values[i:i + window_size]
        sorted_window = sorted(window)
        k = window_size

        if k % 2 == 1:
            median = float(sorted_window[k // 2])
        else:
            median = (sorted_window[k // 2 - 1] + sorted_window[k // 2]) / 2.0

        result.append(median)

    return result