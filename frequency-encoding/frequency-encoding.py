def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here
    count_dic = {}
    for j in values:
        count_dic[j] = 0
    for i in values:
        count_dic[i] += 1
    return [count_dic[v]/len(values) for v in values]