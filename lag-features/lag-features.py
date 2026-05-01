def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    # Write code here
    max_lag = max(lags)
    result = []

    for t in range(max_lag, len(series)):
        row = [series[t - lag] for lag in lags]
        result.append(row)

    return result