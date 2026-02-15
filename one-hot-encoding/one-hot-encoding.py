import numpy as np

def one_hot(y, num_classes=None):
  """
  Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
  """
  # Write code here
  if num_classes == None:
    num_classes = np.max(y) + 1

  N = len(y)
  matrix = np.zeros((N, num_classes))
  matrix[np.arange(N), y] = 1
  return matrix
  pass