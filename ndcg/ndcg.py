import math

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """
    # Write code here    
    # Use only top-k elements
    k = min(k, len(relevance_scores))
    
    def dcg(scores):
        total = 0.0
        for i in range(len(scores)):
            rel = scores[i]
            # position i is 0-based → i+1 for formula
            denom = math.log2(i + 2)  # log2(i+1+1)
            total += (2**rel - 1) / denom
        return total

    # Compute DCG for given ranking
    dcg_val = dcg(relevance_scores[:k])
    
    # Compute IDCG (ideal ranking)
    ideal_scores = sorted(relevance_scores, reverse=True)
    idcg_val = dcg(ideal_scores[:k])
    
    # Edge case: all zeros
    if idcg_val == 0:
        return 0.0
    
    return dcg_val / idcg_val
    pass