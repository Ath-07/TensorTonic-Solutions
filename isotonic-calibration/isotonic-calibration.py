def calibrate_isotonic(cal_labels, cal_probs, new_probs):
    """
    Apply isotonic regression calibration.
    """
    # Write code here
    # Step 1: Sort calibration data
    pairs = sorted(zip(cal_probs, cal_labels))
    p = [x[0] for x in pairs]
    y = [x[1] for x in pairs]
    
    # Step 2: Isotonic regression (PAV)
    stack = []  # each element = [sum, count]
    
    for val in y:
        stack.append([val, 1])
        
        # Merge while violating monotonicity
        while len(stack) >= 2:
            if (stack[-2][0] / stack[-2][1]) > (stack[-1][0] / stack[-1][1]):
                s1, c1 = stack.pop()
                s0, c0 = stack.pop()
                stack.append([s0 + s1, c0 + c1])
            else:
                break
    
    # Expand to calibrated values
    c = []
    for s, count in stack:
        avg = s / count
        c.extend([avg] * count)
    
    # Step 3: Interpolate new probabilities
    result = []
    n = len(p)
    
    for q in new_probs:
        # Clamp
        if q <= p[0]:
            result.append(c[0])
            continue
        if q >= p[-1]:
            result.append(c[-1])
            continue
        
        # Find interval (linear scan is fine for constraints)
        for i in range(n - 1):
            if p[i] <= q <= p[i + 1]:
                val = c[i] + (q - p[i]) / (p[i+1] - p[i]) * (c[i+1] - c[i])
                result.append(val)
                break
    
    return result
    pass