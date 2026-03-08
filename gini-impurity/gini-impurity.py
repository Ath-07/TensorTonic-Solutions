import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    y_left = np.asarray(y_left)
    y_right = np.asarray(y_right)
    l_num = len(y_left)
    r_num = len(y_right)
    l_val, l_count = np.unique(y_left, return_counts=True)
    r_val, r_count = np.unique(y_right, return_counts=True)
    if l_num == 0:
        gini_left = 0     
    else:
        l_prob = np.array([l/l_num for l in l_count])
        gini_left = 1 - np.sum(l_prob**2)
    if r_num == 0:
        gini_right = 0
    else:
        r_prob = np.array([r/r_num for r in r_count])
        gini_right = 1 - np.sum(r_prob**2)
    n = l_num + r_num
    if n == 0:
        return 0.0
    gini_split = ((l_num/n)*gini_left) + ((r_num/n)*gini_right)
    return float(gini_split)
    pass