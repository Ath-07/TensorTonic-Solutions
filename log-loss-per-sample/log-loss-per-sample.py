import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)

    n = len(y_pred)

    y_pred = np.clip(y_pred, eps, 1-eps)

    log_loss_s = [(-1*((y_true[i]*np.log(y_pred[i])+((1-y_true[i])*np.log(1-y_pred[i]))))) for i in range(n)]

    return log_loss_s
    pass