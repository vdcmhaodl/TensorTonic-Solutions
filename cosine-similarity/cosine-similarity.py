import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    n_a = np.linalg.norm(a)
    n_b = np.linalg.norm(b)
    cosin = (a @ b) / (n_a * n_b) if n_a * n_b != 0 else 0.0
    return float(cosin)
    pass