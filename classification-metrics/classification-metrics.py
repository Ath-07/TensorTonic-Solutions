import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    # Map labels to 0..K-1 (handles arbitrary ints)
    labels = np.unique(np.concatenate([y_true, y_pred]))
    label_to_idx = {label: i for i, label in enumerate(labels)}
    y_true_idx = np.vectorize(label_to_idx.get)(y_true)
    y_pred_idx = np.vectorize(label_to_idx.get)(y_pred)

    K = len(labels)

    # Confusion matrix
    cm = np.zeros((K, K), dtype=np.int64)
    np.add.at(cm, (y_true_idx, y_pred_idx), 1)

    # Per-class stats
    TP = np.diag(cm)
    FP = cm.sum(axis=0) - TP
    FN = cm.sum(axis=1) - TP
    support = cm.sum(axis=1)

    # Accuracy (same for all averaging modes)
    accuracy = TP.sum() / cm.sum()

    # Safe division
    def safe_div(a, b):
        return np.divide(a, b, out=np.zeros_like(a, dtype=float), where=b != 0)

    precision_c = safe_div(TP, TP + FP)
    recall_c = safe_div(TP, TP + FN)
    f1_c = safe_div(2 * precision_c * recall_c, precision_c + recall_c)

    # Averaging
    if average == "micro":
        TP_sum = TP.sum()
        FP_sum = FP.sum()
        FN_sum = FN.sum()

        precision = TP_sum / (TP_sum + FP_sum) if (TP_sum + FP_sum) > 0 else 0.0
        recall = TP_sum / (TP_sum + FN_sum) if (TP_sum + FN_sum) > 0 else 0.0
        f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0.0

    elif average == "macro":
        precision = precision_c.mean()
        recall = recall_c.mean()
        f1 = f1_c.mean()

    elif average == "weighted":
        weights = support / support.sum()
        precision = np.sum(weights * precision_c)
        recall = np.sum(weights * recall_c)
        f1 = np.sum(weights * f1_c)

    elif average == "binary":
        if pos_label not in label_to_idx:
            raise ValueError("pos_label not found in labels")

        i = label_to_idx[pos_label]
        precision = precision_c[i]
        recall = recall_c[i]
        f1 = f1_c[i]

    else:
        raise ValueError("Invalid average type")

    return {
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1),
    }