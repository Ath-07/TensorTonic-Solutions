import numpy as np

def compute_gradient_with_skip(gradients_F: list, x: np.ndarray) -> np.ndarray:
    """
    Compute gradient flow through L layers WITH skip connections.
    Gradient at layer l = sum of paths through network
    """
    # YOUR CODE HERE
    result = np.array(x, dtype=float)

    for grad in gradients_F:
        result = result + np.dot(result, grad)

    return result
    pass

def compute_gradient_without_skip(gradients_F: list, x: np.ndarray) -> np.ndarray:
    """
    Compute gradient flow through L layers WITHOUT skip connections.
    """
    # YOUR CODE HERE
    result = np.array(x, dtype=float)

    for grad in gradients_F:
        result = np.dot(result, grad)

    return result
    pass
