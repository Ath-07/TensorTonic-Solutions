import numpy as np

def gini(S):
    S = np.asarray(S)
    n = len(S)
    n_class, counts = np.unique(S, return_counts=True)
    probs = np.array([c/n for c in counts])
    gini_val = 1 - np.sum(probs**2)
    return gini_val

def gini_split(left, right):
    left = np.asarray(left)
    right = np.asarray(right)
    n_l = len(left)
    n_r = len(right)
    n = n_l + n_r
    gini_s = 0
    if n_l > 0:
        gini_s += (n_l/n) * gini(left)
    if n_r > 0:
        gini_s += (n_r/n) * gini(right)
    return gini_s

def decision_tree_split(X, y):
    """
    Find the best feature and threshold to split the data.
    """
    # Write code here
    storage = []
    X = np.asarray(X)
    y = np.asarray(y)
    n_datapoints, n_features = X.shape
    gini_parent = gini(y)
    for i in range(n_features):
        dict_f = {}
        idx = X[:, i].argsort()
        X_sorted = X[idx]
        y_sorted = y[idx]
        feature = X_sorted[:, i]
        thresholds = [(feature[j] + feature[j+1])/2 for j in range(n_datapoints-1) if feature[j] != feature[j+1]]
        for t in thresholds:
            left = []
            right = []
            for d in range(n_datapoints):
                if X_sorted[d, i] <= t:
                    left.append(y_sorted[d])
                else:
                    right.append(y_sorted[d])
            information_gain = gini_parent - gini_split(left, right)
            dict_f[t] = information_gain
        storage.append(dict_f)
    min_thres_feature = {}
    for i in range(len(storage)):
        dict_k = storage[i]
        if len(dict_k) == 0:
            continue
        min_key_value_pair = max(dict_k.items(), key=lambda item: item[1])
        min_key = min_key_value_pair[0]
        min_thres_feature[i] = (min_key, dict_k[min_key])
    best_feature = max(min_thres_feature.items(), key=lambda item: item[1][1])[0]
    best_threshold = min_thres_feature[best_feature][0]
    return (best_feature, best_threshold)            