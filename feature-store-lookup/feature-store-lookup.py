def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    # Write code here
    result = []

    for request in requests:
        user_id = request["user_id"]
        online_features = request["online_features"]

        offline_features = feature_store.get(user_id, defaults)
        combined = {**offline_features, **online_features}

        result.append(combined)

    return result
    pass