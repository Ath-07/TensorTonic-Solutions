import math

def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    log_nor = [math.log(1+v) for v in values]
    return log_nor