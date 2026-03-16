import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here
    tpr = np.asarray(tpr)
    fpr = np.asarray(fpr)

    if len(tpr) != len(fpr) or len(tpr) < 2 or len(fpr) < 2:
        return TypeError
    auc = np.trapezoid(tpr, fpr)
    return float(auc)
    pass