import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    # Write code here
    y_score = np.asarray(y_score)
    y_true = np.asarray(y_true)
    n = len(y_score)

    l_i = [max(0, margin - (y_true[i]*y_score[i])) for i in range(n)]
    l_i = np.asarray(l_i)

    sum = np.sum(l_i)

    if reduction == "mean":
        return sum/n
    if reduction == "sum":
        return sum
    pass