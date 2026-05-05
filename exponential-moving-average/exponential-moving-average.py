def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    # Write code here
    EMA = []
    EMA.append(values[0])
    for i in range(1, len(values)):
        val = alpha * values[i] + ((1-alpha) * EMA[i-1])
        EMA.append(val)

    return EMA