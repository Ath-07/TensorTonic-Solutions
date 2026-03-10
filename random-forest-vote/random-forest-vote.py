import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    results = []
    predictions = np.asarray(predictions)
    n_trees, n_samples = predictions.shape
    for i in range(n_samples):
        sample_preds = predictions[:, i]
        all_class, counts = np.unique(sample_preds, return_counts=True)
        max_idx = np.argmax(counts)
        max_class = all_class[max_idx]
        vote = np.min(max_class)
        results.append(vote)
    return results