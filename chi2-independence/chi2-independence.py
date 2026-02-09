import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    C = np.asarray(C)
    row_totals = C.sum(axis=1, keepdims=True)
    col_totals = C.sum(axis=0, keepdims=True)
    total = C.sum()
    expected = row_totals @ col_totals / total 
    chi2 = np.sum((C - expected) ** 2 / expected)
    return float(chi2), expected
    pass