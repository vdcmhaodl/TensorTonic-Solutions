import numpy as np

def compute_advantage(states: list, rewards: list, V: list, gamma: float) -> np.ndarray:
    """
    Returns the advantages as a NumPy array.
    """
    # Write code here
    returns = [0] * (len(rewards))
    returns[len(rewards) - 1] = rewards[len(rewards) - 1]
    for i in range(len(rewards) - 2, -1, -1):
        returns[i] = returns[i + 1] * gamma + rewards[i]
    baseline = np.asarray(V)[np.asarray(states, dtype=int)]
    returns = np.asarray(returns, dtype=float)
    return np.round(returns - baseline, 4)