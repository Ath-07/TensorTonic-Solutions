def seasonal_average(series, period):
    """
    Compute the average value for each position in the seasonal cycle.
    """
    # Write code here
    out = [0 for _ in range(period)]
    for i in range(period):
        sum = 0
        count = 0
        for j in range(i, len(series), period):
            sum += series[j]
            count += 1
        out [i] = sum / count

    return out