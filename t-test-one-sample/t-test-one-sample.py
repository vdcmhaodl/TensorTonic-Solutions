import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    n = x.shape[0]
    centered_x = x - np.mean(x)
    s = np.sqrt(np.sum(np.square(centered_x)) / (n - 1))
    t = (np.mean(x) - mu0) / (s / np.sqrt(n))
    return float(t)