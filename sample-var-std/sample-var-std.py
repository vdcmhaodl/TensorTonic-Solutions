import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    n = len(x)
    x = np.asarray(x, dtype=float)

    mean = float(np.mean(x))
    variance = float((1.0/(n - 1)) * np.sum(np.square(x - mean)))
    standard_deviation = float(np.sqrt(variance))
    return {
        "variance": variance, 
        "standard_deviation": standard_deviation
    }
    pass