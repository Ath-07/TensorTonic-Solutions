import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    n = len(X_test)
    unique_val, counts = np.unique(y_train, return_counts=True)
    max_ind = np.argmax(counts)
    out = np.full((n,), unique_val[max_ind])
    return out
    pass