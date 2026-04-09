def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    W = np.array(W, dtype=float)
    
    limit = np.sqrt(6.0 / fan_in)
    
    W_scaled = W * (2 * limit) - limit
    
    return W_scaled.tolist()