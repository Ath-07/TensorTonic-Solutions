def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here
    dim = len(points[0])
    
    # Initialize sums and counts
    sums = [[0.0] * dim for _ in range(k)]
    counts = [0] * k
    
    # Accumulate sums
    for point, cluster in zip(points, assignments):
        for d in range(dim):
            sums[cluster][d] += point[d]
        counts[cluster] += 1
    
    # Compute centroids
    centroids = []
    for j in range(k):
        if counts[j] == 0:
            centroids.append([0.0] * dim)
        else:
            centroids.append([s / counts[j] for s in sums[j]])
    
    return centroids