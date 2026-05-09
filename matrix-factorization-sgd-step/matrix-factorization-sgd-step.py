def matrix_factorization_sgd_step(U, V, r, lr, reg):
    """
    Perform one SGD step for matrix factorization.
    """
    # Write code here
    e = r - sum(U[i]*V[i] for i in range(len(U)))
    U_new = [0 for _ in range(len(U))]
    V_new = [0 for _ in range(len(V))]
    for i in range(len(U)):
        U_new[i] = U[i] + lr * ((e*V[i])-(reg*U[i]))
        V_new[i] = V[i] + lr * ((e*U[i])-(reg*V[i]))
    return U_new, V_new