def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    # Matrix transpose
    def transpose(A):
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

    # Matrix multiplication
    def matmul(A, B):
        result = [[0.0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        return result

    # Matrix-vector multiplication
    def matvec(A, v):
        return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]

    # Identity matrix
    def identity(n):
        return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    # Matrix addition
    def add(A, B):
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    # Matrix inverse using Gauss-Jordan elimination
    def inverse(A):
        n = len(A)
        I = identity(n)
        A = [row[:] for row in A]  # copy

        for i in range(n):
            # Pivot
            pivot = A[i][i]
            if pivot == 0:
                for r in range(i + 1, n):
                    if A[r][i] != 0:
                        A[i], A[r] = A[r], A[i]
                        I[i], I[r] = I[r], I[i]
                        pivot = A[i][i]
                        break
            pivot = A[i][i]

            # Normalize row
            for j in range(n):
                A[i][j] /= pivot
                I[i][j] /= pivot

            # Eliminate other rows
            for r in range(n):
                if r != i:
                    factor = A[r][i]
                    for c in range(n):
                        A[r][c] -= factor * A[i][c]
                        I[r][c] -= factor * I[i][c]

        return I

    # ---- Ridge Regression Steps ----
    Xt = transpose(X)
    XtX = matmul(Xt, X)
    d = len(XtX)

    # Add lambda * I
    lamI = [[lam if i == j else 0.0 for j in range(d)] for i in range(d)]
    regularized = add(XtX, lamI)

    # Compute inverse
    reg_inv = inverse(regularized)

    # Compute X^T y
    Xty = matvec(Xt, y)

    # Final weights
    w = matvec(reg_inv, Xty)

    return w















    0