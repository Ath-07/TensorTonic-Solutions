import numpy as np

def pearson_correlation(X):
  """
  Compute Pearson correlation matrix from dataset X.
  """
  # Write code here
  X = np.asarray(X)
  N, D = X.shape
  if N < 2 or X.ndim != 2:
    return None
  else:
    X_mean = np.mean(X, axis = 0)
    X_std = np.std(X, axis = 0, ddof = 1)
    denom = np.outer(X_std, X_std) 
    denom[denom == 0] = np.nan
    X_centered = X - X_mean
    cor_matrix = (1/(N-1))*(X_centered.T @ X_centered)
    R_matrix = cor_matrix / denom
    #np.fill_diagonal(R_matrix, 1.0)
    return R_matrix
  pass