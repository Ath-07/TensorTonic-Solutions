import numpy as np

def poisson_pmf_cdf(lam: float, k: int):
    if lam <= 0 or k < 0:
        raise ValueError("lam must be > 0 and k must be >= 0")

    # log-factorial using vectorized logs (stable, no factorial loop)
    def log_factorial(n):
        if n <= 1:
            return 0.0
        return np.log(np.arange(1, n + 1)).sum()

    # PMF at k (log form for stability)
    log_pmf_k = -lam + k * np.log(lam) - log_factorial(k)
    pmf = float(np.exp(log_pmf_k))

    # CDF = sum PMF(i), i=0..k (vectorized)
    i = np.arange(0, k + 1)
    log_fact = np.zeros(k + 1)
    if k >= 2:
        log_fact[2:] = np.cumsum(np.log(np.arange(2, k + 1)))
    log_pmf = -lam + i * np.log(lam) - log_fact
    cdf = float(np.exp(log_pmf).sum())

    return pmf, cdf