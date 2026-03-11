import numpy as np 

def gaussian_naive_bayes(X_train, y_train, X_test):
    """
    Predict class labels for test samples using Gaussian Naive Bayes.
    """
    # Write code here
    epsilon = 1e-9

    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_test = np.array(X_test)

    classes, counts = np.unique(y_train, return_counts=True)

    priors = {}
    means = {}
    variances = {}
    predictions = []

    for c in classes:
        X_c = X_train[y_train == c]
        priors[c] = X_c.shape[0] / X_train.shape[0]
        means[c] = np.mean(X_c, axis=0)
        variances[c] = np.var(X_c, axis=0) + epsilon

    for x in X_test:
        log_posteriors = []

        for c in classes:
            mean = means[c]
            var = variances[c]

            log_prior = np.log(priors[c])
            log_likelihood = np.sum(
                -0.5 * np.log(2 * np.pi * var) -
                ((x - mean) ** 2) / (2 * var)
            )

            log_posteriors.append(log_prior + log_likelihood)

        predictions.append(classes[np.argmax(log_posteriors)])

    return predictions
