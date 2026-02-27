def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code here
    sorted_vals = sorted(values)
    n = len(values)
    
    if n == 0:
        return []
    if n == 1:
        return [0]
    
    if n % 2 == 1:
        mid = int(n/2)
        median = sorted_vals[mid]
        half_1 = sorted_vals[:mid]
        half_2 = sorted_vals[mid+1:]
    else:
        mid_1 = int((n-1)/2)
        mid_2 = int(n/2)
        median = (sorted_vals[mid_1] + sorted_vals[mid_2]) / 2
        half_1 = sorted_vals[:mid_1+1]
        half_2 = sorted_vals[mid_2:]
    
    a = len(half_1)
    b = len(half_2)

    if a % 2 == 1:
        mid = int(a/2)
        Q1 = half_1[mid]
    else:
        mid_1 = int((a-1)/2)
        mid_2 = int(a/2)
        Q1 = (half_1[mid_1] + half_1[mid_2]) / 2

    if b % 2 == 1:
        mid = int(b/2)
        Q3 = half_2[mid]
    else:
        mid_1 = int((b-1)/2)
        mid_2 = int(b/2)
        Q3 = (half_2[mid_1] + half_2[mid_2]) / 2

    if Q3 == Q1:
        return [(v-median) for v in values]
    else:
        return [((v-median)/(Q3-Q1)) for v in values]
