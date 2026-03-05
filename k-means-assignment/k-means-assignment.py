def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    assignments = []

    for p in points:
        best_dist = float('inf')
        best_idx = 0

        for j, c in enumerate(centroids):
            # compute squared Euclidean distance
            dist = sum((p[d] - c[d]) ** 2 for d in range(len(p)))

            if dist < best_dist:
                best_dist = dist
                best_idx = j

        assignments.append(best_idx)

    return assignments
    