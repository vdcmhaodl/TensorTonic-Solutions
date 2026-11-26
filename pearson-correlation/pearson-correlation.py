import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    N = X.shape[0]
    centered = X - np.mean(X, axis=0)
    Cov = centered.T @ centered / (N - 1)
    std = np.sqrt(np.diag(Cov))
    denominator = np.outer(std, std)
    corr = Cov / denominator
    return corr