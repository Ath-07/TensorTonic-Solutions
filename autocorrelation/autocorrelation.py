def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    # Write code here
    x_sum = 0
    var = 0
    out = [1.0]
    
    for i in range(len(series)):
        x_sum += series[i]

    mean = x_sum / len(series)

    for i in range(len(series)):
        var += (series[i] - mean)**2

    if var == 0:
        return [1.0] + [0.0]*max_lag

    for i in range(1, max_lag+1):
        cross_sum = 0
        for j in range(len(series)-i):
            cross_sum += (series[j] - mean) * (series[j+i] - mean)
        out.append(cross_sum/var)

    return out
            
    