import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    # Positions: (T, 1)
    pos = np.arange(seq_len)[:, np.newaxis]
    
    # Dimension indices for sin/cos pairs: (1, ceil(d_model/2))
    i = np.arange((d_model + 1) // 2)[np.newaxis, :]
    
    # Compute the denominator term: base^(2i / d_model)
    denom = base ** (2 * i / d_model)
    
    # Compute angles: (T, ceil(d_model/2))
    angles = pos / denom
    
    # Initialize output
    pe = np.zeros((seq_len, d_model))
    
    # Fill even indices (sin)
    pe[:, 0::2] = np.sin(angles[:, :pe[:, 0::2].shape[1]])
    
    # Fill odd indices (cos)
    pe[:, 1::2] = np.cos(angles[:, :pe[:, 1::2].shape[1]])
    
    return pe
    pass