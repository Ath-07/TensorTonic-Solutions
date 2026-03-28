import numpy as np

def roc_curve(y_true, y_score):
    """
    Compute ROC curve from binary labels and scores.
    """
    # Write code here
    y_score = np.asarray(y_score)
    y_true = np.asarray(y_true)

    order = np.argsort(-y_score, kind="mergesort")
    y_true = y_true[order]
    y_score = y_score[order]

    P = np.sum(y_true == 1)
    N = np.sum(y_true == 0)

    TP = np.cumsum(y_true == 1)
    FP = np.cumsum(y_true == 0)

    distinct_idx = np.where(np.diff(y_score))[0]
    threshold_idxs = np.r_[distinct_idx, len(y_score) - 1]

    TP = TP[threshold_idxs]
    FP = FP[threshold_idxs]
    thresholds = y_score[threshold_idxs]

    TPR = TP / P if P > 0 else np.zeros_like(TP, dtype=float)
    FPR = FP / N if N > 0 else np.zeros_like(FP, dtype=float)

    TPR = np.r_[0.0, TPR]
    FPR = np.r_[0.0, FPR]
    thresholds = np.r_[np.inf, thresholds]

    return FPR, TPR, thresholds
    pass