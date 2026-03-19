import numpy as np

def kl_divergence(p, q, eps=1e-12):
    """
    Compute KL Divergence D_KL(P || Q).
    """
    # Write code here
    p = np.asarray(p)
    q = np.asarray(q)
    n = len(p)

    q_stable = q + eps

    each_kl = [p[i] * np.log(p[i]/q[i]) if p[i] != 0 else 0 for i in range(n)]
    each_kl = np.asarray(each_kl)
    
    total_kl = np.sum(each_kl)

    return total_kl
    pass