def bigram_probabilities(tokens):
    """
    Returns: (counts, probs)
      counts: dict mapping (w1, w2) -> integer count
      probs: dict mapping (w1, w2) -> float P(w2 | w1) with add-1 smoothing
    """
    # Your code here
    if not tokens:
        return {}, {}
    
    vocab = sorted(set(tokens))
    V = len(vocab)
    
    bigram_counts = {}
    context_counts = {}
    
    for i in range(len(tokens) - 1):
        w1 = tokens[i]
        w2 = tokens[i + 1]
        
        if (w1, w2) in bigram_counts:
            bigram_counts[(w1, w2)] += 1
        else:
            bigram_counts[(w1, w2)] = 1
            
        if w1 in context_counts:
            context_counts[w1] += 1
        else:
            context_counts[w1] = 1
    
    probs = {}
    
    for w1 in vocab:
        denom = context_counts.get(w1, 0) + V
        
        for w2 in vocab:
            count = bigram_counts.get((w1, w2), 0)
            probs[(w1, w2)] = (count + 1) / denom
    
    return bigram_counts, probs
    pass