import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    y = np.asarray(y, dtype=int)
    num_classes = np.max(y) + 1 if num_classes == None else num_classes
    OneHot = np.zeros((y.shape[0], int(num_classes)), dtype=float)
    OneHot[np.arange(y.shape[0]), y] = 1.0
    print(OneHot)
    return OneHot