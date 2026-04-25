def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    H = 0
    for i in range(len(actual_tokens)):
        pi = prob_distributions[i][actual_tokens[i]]
        H += math.log(pi)

    H = (-1/len(actual_tokens)) * H
    PP = math.exp(H)
    return PP