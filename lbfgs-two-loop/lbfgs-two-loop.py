def _dot(a, b):
    """Dot product of two vectors."""
    return sum(x * y for x, y in zip(a, b))

def lbfgs_direction(grad, s_list, y_list):
    """
    Compute the L-BFGS search direction using the two-loop recursion.
    """
    # Write code here
    m = len(s_list)
    
    # Step 1: Precompute rho values
    rho = [1.0 / _dot(y_list[i], s_list[i]) for i in range(m)]
    
    # Step 2: Backward loop
    q = grad[:]  # copy
    alpha = [0.0] * m
    
    for i in reversed(range(m)):
        alpha[i] = rho[i] * _dot(s_list[i], q)
        q = [q_j - alpha[i] * y_ij for q_j, y_ij in zip(q, y_list[i])]
    
    # Step 3: Initial scaling (gamma)
    s_last = s_list[-1]
    y_last = y_list[-1]
    
    gamma = _dot(s_last, y_last) / _dot(y_last, y_last)
    
    # Step 4: Apply initial Hessian approximation
    r = [gamma * q_j for q_j in q]
    
    # Step 5: Forward loop
    for i in range(m):
        beta = rho[i] * _dot(y_list[i], r)
        r = [
            r_j + s_ij * (alpha[i] - beta)
            for r_j, s_ij in zip(r, s_list[i])
        ]
    
    # Step 6: Return descent direction
    return [-r_j for r_j in r]