import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)

    classes = np.unique(np.concatenate([y_true, y_pred]))

    TP = FP = FN = 0

    for c in classes:
        TP += np.sum((y_pred == c) & (y_true == c))
        FP += np.sum((y_pred == c) & (y_true != c))
        FN += np.sum((y_pred != c) & (y_true == c))

    return (2 * TP) / (2 * TP + FP + FN)
    pass