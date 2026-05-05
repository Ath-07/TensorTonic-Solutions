def double_exponential_smoothing(series, alpha, beta):
    """
    Apply Holt's linear trend method and return the level values.
    """
    # Write code here
    level = float(series[0])
    trend = float(series[1] - series[0])
    
    result = [level]
    
    for t in range(1, len(series)):
        value = series[t]
        
        new_level = alpha * value + (1 - alpha) * (level + trend)
        new_trend = beta * (new_level - level) + (1 - beta) * trend
        
        level, trend = new_level, new_trend
        result.append(level)
    
    return result