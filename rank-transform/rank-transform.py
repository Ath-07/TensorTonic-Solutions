def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here
    sort_val = sorted(values)
    i = 0
    mapping = {}
    n = len(sort_val)
    while i < n:
        j = i
        # Find range of tied values
        while j + 1 < n and sort_val[j] == sort_val[j + 1]:
            j += 1
        # Step 3: Compute average rank (1-based indexing)
        avg_rank = (i + 1 + j + 1) / 2.0
        # Step 4: Store mapping
        mapping[sort_val[i]] = avg_rank
        i = j + 1
    
    # Step 5: Build result preserving original order
    return [float(mapping[val]) for val in values]