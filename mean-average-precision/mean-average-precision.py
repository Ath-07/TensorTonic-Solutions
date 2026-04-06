import numpy as np

def mean_average_precision(y_true_list, y_score_list, k=None):
    """
    Compute Mean Average Precision (mAP) for multiple retrieval queries.
    """
    # Write code here
    if len(y_true_list) != len(y_score_list):
        raise ValueError("Mismatched inputs")

    ap_list = []

    for y_true, y_score in zip(y_true_list, y_score_list):
        y_true = np.asarray(y_true)
        y_score = np.asarray(y_score)
        if y_true.shape != y_score.shape:
            raise ValueError("Shape mismatch within a entry of input")

        # Sort by descending score
        order = np.argsort(-y_score)
        y_true_sorted = y_true[order]
        
        # Apply cutoff k if provided
        if k is not None:
            y_true_sorted = y_true_sorted[:k]

        # Total relevant items (in full list, not truncated)
        R = np.sum(y_true)

        if R == 0:
            ap_list.append(0.0)
            continue
        
        # Cumulative sum of relevant items
        cumsum_rel = np.cumsum(y_true_sorted)

        # Ranks (1-based)
        ranks = np.arange(1, len(y_true_sorted) + 1)
        
        # Precision at each rank
        precision_at_k = cumsum_rel / ranks
        
        # Only keep positions where item is relevant
        ap = np.sum(precision_at_k * y_true_sorted) / R
        
        ap_list.append(ap)

    # Mean Average Precision
    map_value = float(np.mean(ap_list)) if ap_list else 0.0
    return map_value, ap_list
    pass