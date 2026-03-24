def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    # Write code here
    K = len(predictions)
    q=[]
    for i in range(K):
        if i == target:
            q.append((1-epsilon) + (epsilon/K))
        else:
            q.append(epsilon/K)
    loss = 0
    eps=1e-12
    for i in range(K):
        loss += q[i] * math.log(max(predictions[i], eps))
    return -loss