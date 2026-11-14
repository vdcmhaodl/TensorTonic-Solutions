import numpy as np
def compute_monitoring_metrics(system_type: str, y_true: list, y_pred: list) -> dict:
    """
    Returns a dictionary of metrics.
    """
    N = len(y_true)
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    if system_type == 'classification':
        TP = np.sum((y_true == 1) & (y_pred == 1))
        TN = np.sum((y_true == 0) & (y_pred == 0))
        FP = np.sum((y_true == 0) & (y_pred == 1))
        FN = np.sum((y_true == 1) & (y_pred == 0)) 
        acc = (TP + TN) / N
        pre = TP / (TP + FP) if (TP + FP) else 0.0
        recall = TP / (TP + FN) if (TP + FN) else 0.0
        F1 = (2.0 * pre * recall) / (pre + recall) if (pre + recall) else 0.0
        ans = {
            "accuracy": acc,
            "precision": pre,
            "recall": recall,
            "f1": F1,
        }
        return ans
    elif system_type == 'regression':
        mae = np.mean(np.abs(y_true - y_pred))
        rmse = np.sqrt(np.mean(np.square((y_true - y_pred))))
        ans = {
            "mae": mae,
            "rmse": rmse,
        }
        return ans
    else:
        sorted_pair = sorted(range(N), key=lambda i: y_pred[i], reverse=True)
        top3 = sorted_pair[:3]
        h = np.sum(y_true[top3])
        return {
            "precision_at_3": h / 3,
            "recall_at_3": h / np.sum(y_true) if np.sum(y_true) > 0 else 0.0
        }