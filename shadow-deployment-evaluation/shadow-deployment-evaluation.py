def evaluate_shadow(production_log, shadow_log, criteria):
    """
    Evaluate whether a shadow model is ready for promotion.
    """
    # Write code here
    n = len(production_log)

    # Accuracy
    production_correct = 0
    shadow_correct = 0

    # Agreement
    agreement_count = 0

    # Shadow latencies
    shadow_latencies = []

    for p, s in zip(production_log, shadow_log):

        if p["prediction"] == p["actual"]:
            production_correct += 1

        if s["prediction"] == s["actual"]:
            shadow_correct += 1

        if p["prediction"] == s["prediction"]:
            agreement_count += 1

        shadow_latencies.append(s["latency_ms"])

    production_accuracy = production_correct / n
    shadow_accuracy = shadow_correct / n
    accuracy_gain = shadow_accuracy - production_accuracy
    agreement_rate = agreement_count / n

    # P95 latency using nearest-rank method
    shadow_latencies.sort()

    index = math.ceil(0.95 * n) - 1
    shadow_latency_p95 = shadow_latencies[index]

    # Promotion decision
    promote = (
        accuracy_gain >= criteria["min_accuracy_gain"]
        and shadow_latency_p95 <= criteria["max_latency_p95"]
        and agreement_rate >= criteria["min_agreement_rate"]
    )

    return {
        "promote": promote,
        "metrics": {
            "shadow_accuracy": shadow_accuracy,
            "production_accuracy": production_accuracy,
            "accuracy_gain": accuracy_gain,
            "shadow_latency_p95": shadow_latency_p95,
            "agreement_rate": agreement_rate
        }
    }
    pass