def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    # Write code here
    code = {}
    uni_count = len(ordering)
    for i in range(uni_count):
        code[ordering[i]] = i
    encoded = [code[val] for val in values]
    return encoded