def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here
    ref_total = sum(reference_counts)
    prod_total = sum(production_counts)

    ref_dist = [x / ref_total for x in reference_counts]
    prod_dist = [x / prod_total for x in production_counts]

    tvd = 0.5 * sum(abs(p - q) for p, q in zip(ref_dist, prod_dist))

    return {
        "score": tvd,
        "drift_detected": tvd > threshold
    }
    pass