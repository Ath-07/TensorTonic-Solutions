def compute_monitoring_metrics(system_type, y_true, y_pred):
    """
    Compute the appropriate monitoring metrics for the given system type.
    """
    # Write code here
    metrics = {}

    if system_type == "classification":
        tp = fp = fn = tn = 0

        for yt, yp in zip(y_true, y_pred):
            if yt == 1 and yp == 1:
                tp += 1
            elif yt == 0 and yp == 1:
                fp += 1
            elif yt == 1 and yp == 0:
                fn += 1
            else:
                tn += 1

        n = len(y_true)

        accuracy = (tp + tn) / n

        precision = tp / (tp + fp) if (tp + fp) else 0.0
        recall = tp / (tp + fn) if (tp + fn) else 0.0

        f1 = (
            2 * precision * recall / (precision + recall)
            if (precision + recall)
            else 0.0
        )

        metrics["accuracy"] = accuracy
        metrics["precision"] = precision
        metrics["recall"] = recall
        metrics["f1"] = f1

    elif system_type == "regression":
        n = len(y_true)

        abs_errors = [abs(a - b) for a, b in zip(y_true, y_pred)]
        sq_errors = [(a - b) ** 2 for a, b in zip(y_true, y_pred)]

        mae = sum(abs_errors) / n
        rmse = ((sum(sq_errors) / n)**0.5)

        metrics["mae"] = mae
        metrics["rmse"] = rmse

    elif system_type == "ranking":
        ranked = sorted(
            zip(y_true, y_pred),
            key=lambda x: x[1],
            reverse=True
        )

        top_k = ranked[:3]

        relevant_in_top3 = sum(label for label, _ in top_k)
        total_relevant = sum(y_true)

        precision_at_3 = relevant_in_top3 / 3
        recall_at_3 = (
            relevant_in_top3 / total_relevant
            if total_relevant
            else 0.0
        )

        metrics["precision_at_3"] = precision_at_3
        metrics["recall_at_3"] = recall_at_3

    return sorted(metrics.items())
    pass