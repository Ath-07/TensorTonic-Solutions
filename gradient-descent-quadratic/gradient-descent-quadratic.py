def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    out = x0
    for i in range(steps):
        grad = (2 * a * out) + b
        out = out - (lr * grad)
    return out
    pass