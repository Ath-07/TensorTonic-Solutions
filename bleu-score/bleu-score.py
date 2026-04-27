import math
def get_ngram_counts(tokens, n):
    counts = {}
    for i in range(len(tokens) - n + 1):
        ng = tuple(tokens[i:i+n])
        if ng in counts:
            counts[ng] += 1
        else:
            counts[ng] = 1
    return counts

def bleu_score(candidate, reference, max_n):
    """
    Compute the BLEU score for a candidate translation.
    """
    # Write code here
    if len(candidate) == 0:
        return 0.0

    c_len = len(candidate)
    r_len = len(reference)

    precisions = []

    for n in range(1, max_n + 1):
        cand_counts = get_ngram_counts(candidate, n)
        ref_counts = get_ngram_counts(reference, n)

        total = 0
        clipped = 0

        for ng in cand_counts:
            count_c = cand_counts[ng]
            count_r = ref_counts.get(ng, 0)

            clipped += min(count_c, count_r)
            total += count_c

        if total == 0:
            return 0.0

        p_n = clipped / total

        if p_n == 0:
            return 0.0

        precisions.append(p_n)

    if c_len >= r_len:
        bp = 1.0
    else:
        bp = math.exp(1 - r_len / c_len)

    log_sum = 0.0
    for p in precisions:
        log_sum += math.log(p)

    log_mean = log_sum / max_n
    bleu = bp * math.exp(log_mean)

    return bleu
