def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here
    out = [0 for _ in range(len(series)-1)]
    for i in range(1, len(series)):
        if series[i-1] == 0:
            out[i-1] = 0
        else:
            out[i-1] = (series[i]-series[i-1]) / (series[i-1])

    return out