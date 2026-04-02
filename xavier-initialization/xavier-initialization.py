def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Write code here
    bound = math.sqrt(6/(fan_in+fan_out))
    mapped = [[v * (2*bound) - bound for v in row] for row in W]
    return mapped