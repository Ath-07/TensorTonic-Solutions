import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Write code here
    X = np.asarray(X)
    NaN_pos = np.isnan(X)
    if strategy == 'mean':
        mean = np.nanmean(X, axis=0)
        mean = np.where(np.isnan(mean), 0, mean)
        Final_arr = np.nan_to_num(X, nan=mean)
    if strategy == 'median':
        median = np.nanmedian(X, axis=0)        
        median = np.where(np.isnan(median), 0, median)
        Final_arr = np.nan_to_num(X, nan=median)
    return Final_arr
    pass