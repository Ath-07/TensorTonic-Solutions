import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    # Write code here
    p = np.asarray(p)
    y = np.asarray(y)
    py = p * y

    dice_coe = ((2*np.sum(py)) + eps)/(np.sum(p) + np.sum(y) + eps)
    dice_l = 1- dice_coe
    return dice_l
    pass