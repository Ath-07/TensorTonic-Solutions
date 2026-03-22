def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    # Write code here
    n = len(predictions)
    fl = 0
    for i in range(n):
        if (targets[i] == 1):
            pt = predictions[i]
        if (targets[i] == 0):
            pt = 1 - predictions[i]
        each_fl = (-1) * alpha * ((1-pt)**gamma)* math.log(pt)
        fl += each_fl
    return (1/n)*fl