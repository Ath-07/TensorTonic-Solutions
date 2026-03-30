def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    ELU = []
    for v in x:
        if v > 0:
            ELU.append(v)
        else:
            ELU.append(alpha * (math.exp(v) - 1))
    return ELU