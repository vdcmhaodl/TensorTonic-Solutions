import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    x = np.asarray(x, dtype=int)

    pmf = (p ** x) * ((1 - p) ** (1-x))
    mean = float(p)
    var = p * (1.0 - p)
    return {
        "pmf": pmf,
        "mean": mean,
        "variance": var
    }
    pass