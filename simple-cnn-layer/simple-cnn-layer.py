import numpy as np

def conv2d(x, W, b):
    """
    Simple 2D convolution layer forward pass.
    Valid padding, stride=1.
    """
    # Write code here
    x = np.asarray(x)
    N, C_in, H, W_in = x.shape
    C_out, _, KH, KW = W.shape
    
    H_out = H - KH + 1
    W_out = W_in - KW + 1
    
    # Initialize output
    y = np.zeros((N, C_out, H_out, W_out), dtype=float)
    
    # Slide kernel over spatial positions
    for i in range(H_out):
        for j in range(W_out):
            # Extract patch: (N, C_in, KH, KW)
            patch = x[:, :, i:i+KH, j:j+KW]
            
            # Compute convolution:
            # Expand dims for broadcasting:
            # patch -> (N, 1, C_in, KH, KW)
            # W     -> (1, C_out, C_in, KH, KW)
            patch_exp = patch[:, None, :, :, :]
            W_exp = W[None, :, :, :, :]
            
            # Elementwise multiply and sum
            y[:, :, i, j] = np.sum(patch_exp * W_exp, axis=(2, 3, 4))
    
    # Add bias (broadcast over N, H_out, W_out)
    y += b[None, :, None, None]
    
    return y
    pass