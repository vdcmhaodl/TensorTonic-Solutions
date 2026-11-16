import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    L = max_len if max_len else max((len(seq) for seq in seqs), default=0)
    N = len(seqs)
    ans = np.full((N, L), pad_value)
    for i in range(N):
        for j in range(len(seqs[i])):
            if j >= L: break
            ans[i][j] = seqs[i][j]
    return ans
    pass