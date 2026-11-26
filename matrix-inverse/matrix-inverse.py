import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    # Write code here
    A = np.asarray(A, dtype=float)
    n = A.shape[0]
    AandI = np.concatenate((A, np.eye(n)), axis=1)
    for column in range(n):
        pivot = column + np.argmax(np.abs(AandI[column:, column]))
        if abs(AandI[pivot, column]) < 1e-12:
            return None
        AandI[[column, pivot]] = AandI[[pivot, column]]
        AandI[column] /= AandI[column, column]
        for row in range(n):
            if row != column:
                AandI[row] -= AandI[row, column] * AandI[column]
    return AandI[:, n:]