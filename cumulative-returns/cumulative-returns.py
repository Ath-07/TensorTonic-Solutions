def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    # Write code here
    out = []
    w = 1
    for i in range(len(returns)):
        w *= (1+returns[i])
        cum_r = w - 1
        out.append(cum_r)

    return out