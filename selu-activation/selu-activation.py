import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    # Write code here
    x = np.asarray(x)
    out = []
    for v in x:
        if v > 0:
            out.append(lam*v)
        else:
            out.append(alpha*lam*(np.exp(v)-1))
    return out
    pass
