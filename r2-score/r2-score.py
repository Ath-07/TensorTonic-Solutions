import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)

    uni_pred, pred_count = np.unique(y_pred, return_counts=True)
    uni_true, true_count = np.unique(y_true, return_counts=True)

    if len(uni_true) == 1 and len(uni_true) == 1 and uni_pred.all() == uni_true.all():
        return 1.0
    if len(uni_true) == 1 and (len(uni_true) != 1 or uni_pred.all() != uni_true.all()):
        return 0.0

    y_mean = np.mean(y_true)
    SSR = np.sum((y_true - y_pred)**2)
    SST = np.sum((y_true - y_mean)**2)
    R2 = 1 - (SSR/SST)
    return R2
    pass