import numpy as np

def naive_bayes_bernoulli(X_train, y_train, X_test):
    """
    Compute log-likelihood P(y|x) for Bernoulli Naive Bayes.
    """
    # Write code here
    X_train = np.asarray(X_train)
    X_test = np.asarray(X_test)
    y_train = np.asarray(y_train)

    classes, count = np.unique(y_train, return_counts=True)
    n_datapoints, n_features = X_train.shape
    n_test = X_test.shape[0]
    n_classes = len(classes)

    log_probs = np.zeros((n_test, n_classes))
    for idx, c in enumerate(classes):
        Xc = X_train[y_train==c]
        nc = len(Xc)

        log_prior = np.log(nc/n_datapoints)
        theta = (np.sum(Xc, axis=0) + 1) / (nc + 2)
        log_theta = np.log(theta)
        log_comp_theta = np.log(1-theta)

        log_likelihood = X_test @ log_theta + (1 - X_test) @ log_comp_theta
        log_probs[:, idx] = log_prior + log_likelihood

    return log_probs 
    pass