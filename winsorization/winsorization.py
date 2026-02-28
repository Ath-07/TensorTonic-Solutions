def winsorize(values, lower_pct, upper_pct):
    """
    Clip values at the given percentile bounds.
    """
    # Write code here
    n = len(values)
    values = sorted(values)
    lb_in = (n-1) * lower_pct / 100
    if lb_in.is_integer():
        k_down = lb_in
    else:
        k_down = lb_in + 1
    lb = values[int(lb_in)] + (lb_in - int(lb_in)) * (values[int(k_down)] - values[int(lb_in)])
    ub_in = (n-1) * upper_pct / 100
    if ub_in.is_integer():
        k_up = ub_in
    else:
        k_up = ub_in + 1
    ub = values[int(ub_in)] + (ub_in - int(ub_in)) * (values[int(k_up)] - values[int(ub_in)])
    out = []
    for val in values:
        if val < lb:
            out.append(lb)
        elif val > ub:
            out.append(ub)
        else:
            out.append(val)
    return out