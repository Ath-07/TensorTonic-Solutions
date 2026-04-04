def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    out = {}
    for i in sentences:
        sen = i
        for j in sen:
            if j in out:
                out[j] += 1
            else:
                out[j] = 1
                
    return out
    pass