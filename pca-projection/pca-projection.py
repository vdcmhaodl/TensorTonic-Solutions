import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    N = X.shape[0]
    centered = X - np.mean(X, axis=0)
    Cov = (centered.T @ centered) / (N - 1)
    eigenvalues, eigenvectors = np.linalg.eigh(Cov)

    idx = np.argsort(eigenvalues)[::-1]
    W = eigenvectors[:, idx[:k]]
    # print(eigenvectors)
    return centered @ W
    pass