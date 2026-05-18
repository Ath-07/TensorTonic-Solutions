import numpy as np

def detect_skew(train_dist, serving_dist, threshold=0.2, eps=1e-10):
    """
    Detect train-serving skew using PSI.
    """
    # Write code here
    results = {}

    for feature in train_dist:
        train = np.array(train_dist[feature], dtype=float)
        serving = np.array(serving_dist[feature], dtype=float)

        train = train + eps
        serving = serving + eps

        psi = np.sum((serving - train) * np.log(serving / train))

        results[feature] = {
            "psi": float(psi),
            "skewed": bool(psi >= threshold)
        }

    return results
    pass