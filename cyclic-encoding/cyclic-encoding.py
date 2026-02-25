import math

def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    # Write code here
    theta_all = [(2*math.pi*v/period) for v in values]
    encoded = [[math.sin(theta), math.cos(theta)] for theta in theta_all]
    return encoded