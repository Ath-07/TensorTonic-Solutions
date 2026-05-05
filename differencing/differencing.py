def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    result = series[:]  # make a copy
    
    for _ in range(order):
        result = [result[i] - result[i - 1] for i in range(1, len(result))]
    
    return result