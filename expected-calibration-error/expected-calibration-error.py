def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    # Write code here
    n = len(y_true)
    bin_size = 1.0 / n_bins
    
    # Initialize bins
    bin_counts = [0] * n_bins
    bin_true_sum = [0.0] * n_bins
    bin_pred_sum = [0.0] * n_bins
    
    # Assign samples to bins
    for y, p in zip(y_true, y_pred):
        if p == 1.0:
            bin_idx = n_bins - 1
        else:
            bin_idx = int(p * n_bins)
        
        bin_counts[bin_idx] += 1
        bin_true_sum[bin_idx] += y
        bin_pred_sum[bin_idx] += p
    
    # Compute ECE
    ece = 0.0
    for i in range(n_bins):
        if bin_counts[i] == 0:
            continue
        
        acc = bin_true_sum[i] / bin_counts[i]
        conf = bin_pred_sum[i] / bin_counts[i]
        weight = bin_counts[i] / n
        
        ece += weight * abs(acc - conf)
    
    return ece
    pass