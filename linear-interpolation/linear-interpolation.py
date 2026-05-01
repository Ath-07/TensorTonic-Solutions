def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    # Write code here
    result = values[:]  
    n = len(values)
    
    i = 0
    while i < n:
        if result[i] is None:
            left = i - 1
            
            right = i
            while right < n and result[right] is None:
                right += 1
            
            v_left = result[left]
            v_right = result[right]
            
            for j in range(left + 1, right):
                fraction = (j - left) / (right - left)
                result[j] = v_left + fraction * (v_right - v_left)
            
            i = right 
        else:
            i += 1
    
    return result