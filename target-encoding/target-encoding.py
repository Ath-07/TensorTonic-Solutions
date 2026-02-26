def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    count = {}
    sum = {}
    n = len(targets)
    for i in range(n):
        count[categories[i]] = 0
        sum[categories[i]] = 0
    for i in range(n):
        sum[categories[i]] += targets[i]
        count[categories[i]] += 1
    out = [sum[categories[i]]/count[categories[i]] for i in range(n)]
    return out
    
        