import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    p = np.asarray(p)
    y = np.asarray(y)
    n = len(p)

    fl_each = [((-1)*((1-p[i])**gamma)*y[i]*np.log(p[i])) - ((p[i]**gamma)*(1-y[i])*np.log(1-p[i])) for i in range(n)]

    fl = (1/n) * np.sum(fl_each)
    return fl
    pass