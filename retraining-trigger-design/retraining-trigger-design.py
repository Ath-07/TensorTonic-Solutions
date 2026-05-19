def retraining_policy(daily_stats, config):
    """
    Decide which days to trigger model retraining.
    """
    # Write code here
    drift_threshold = config["drift_threshold"]
    performance_threshold = config["performance_threshold"]
    max_staleness = config["max_staleness"]
    cooldown = config["cooldown"]
    retrain_cost = config["retrain_cost"]
    budget = config["budget"]

    retrain_days = []

    # Cooldown initially satisfied
    last_retrain_day = -cooldown

    days_since_retrain = 0

    for stats in daily_stats:
        day = stats["day"]
        drift_score = stats["drift_score"]
        performance = stats["performance"]

        days_since_retrain += 1

        drift_trigger = drift_score > drift_threshold
        performance_trigger = performance < performance_threshold
        staleness_trigger = days_since_retrain >= max_staleness

        should_trigger = (drift_trigger or performance_trigger or staleness_trigger)

        cooldown_ok = (day - last_retrain_day) >= cooldown
        budget_ok = budget >= retrain_cost

        if should_trigger and cooldown_ok and budget_ok:
            retrain_days.append(day)

            budget -= retrain_cost
            last_retrain_day = day
            days_since_retrain = 0

    return retrain_days
    pass