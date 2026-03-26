import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    r1 = np.array(rater1)
    r2 = np.array(rater2)
    n = len(r1)
    
    # Step 1: Observed agreement
    p_o = np.sum(r1 == r2) / n
    
    # Step 2: Get all unique labels
    labels = np.union1d(r1, r2)
    
    # Step 3: Expected agreement
    p_e = 0.0
    for label in labels:
        p1 = np.sum(r1 == label) / n
        p2 = np.sum(r2 == label) / n
        p_e += p1 * p2
    
    # Step 4: Edge case
    if p_e == 1:
        return 1.0
    
    # Step 5: Kappa
    return (p_o - p_e) / (1 - p_e)
    pass