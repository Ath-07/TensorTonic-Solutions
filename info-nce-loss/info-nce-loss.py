import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    # Write code here
    z1 = np.asarray(Z1)
    z2 = np.asarray(Z2)
    N, D = z1.shape

    S = (z1 @ z2.T) / temperature
    
    S_max = np.max(S, axis=1, keepdims=True)
    S_stable = S - S_max
    
    exp_S = np.exp(S_stable)
    diag = np.diag(exp_S)
    denom = np.sum(exp_S, axis=1)
    loss = -np.mean(np.log(diag / denom))

    return loss
    pass