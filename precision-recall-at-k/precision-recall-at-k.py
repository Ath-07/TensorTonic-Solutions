def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    rel = set(relevant)
    topk = set(recommended[:k])
    inter = topk & rel

    return [len(inter)/k, len(inter)/len(relevant)]