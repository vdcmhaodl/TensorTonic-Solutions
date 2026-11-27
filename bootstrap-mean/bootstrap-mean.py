import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    n = x.shape[0]
    rng = np.random.default_rng(seed)
    indices = rng.integers(0, n, size=(n_bootstrap, n))
    resamples = x[indices]
    boots_mean = np.mean(resamples, axis=1)
    alpha = (1 - ci) / 2
    lower, upper = np.quantile(boots_mean, [alpha, 1 - alpha])
    bootstrap_mean = np.mean(boots_mean)
    return {
        "bootstrap_mean": float(bootstrap_mean),
        "lower": float(lower),
        "upper": float(upper),
    }