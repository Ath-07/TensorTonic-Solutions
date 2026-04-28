def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here
    out = [0 for _ in range(len(values)-window_size+1)]
    for i in range(len(values)-window_size+1):
        sum = 0
        for j in range(window_size):
            sum += values[i+j]
        out[i] = (1/window_size) * sum

    return out