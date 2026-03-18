import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)
    n = len(y_true)
    
    e = y_true - y_pred
    h_ind = np.where(abs(e) <= delta, (1/2)*(e**2), delta*(abs(e) - (1/2*(delta))))
    loss = (1/n)*(np.sum(h_ind))
    return loss
    pass