import numpy as np
from collections import Counter
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    """
    Returns numpy array of BM25 scores for each document.
    """
    # Write code here
    N = len(docs)
    if N == 0:
        return np.array([], dtype=float)

    doc_lens = np.array([len(doc) for doc in docs], dtype=float)
    avgdl = np.mean(doc_lens) if N > 0 else 0.0

    tf_docs = []
    for doc in docs:
        tf = {}
        for token in doc:
            tf[token] = tf.get(token, 0) + 1
        tf_docs.append(tf)

    df = {}
    for doc in docs:
        seen = set(doc)
        for token in seen:
            df[token] = df.get(token, 0) + 1

    seen_q = set()
    unique_query = []
    for t in query_tokens:
        if t not in seen_q:
            seen_q.add(t)
            unique_query.append(t)

    scores = np.zeros(N, dtype=float)


    for t in unique_query:
        
        df_t = df.get(t, 0)
        if df_t == 0:
            continue

        idf = math.log((N - df_t + 0.5) / (df_t + 0.5) + 1)

        for i in range(N):
            tf = tf_docs[i].get(t, 0)
            if tf == 0:
                continue

            denom = tf + k1 * (1 - b + b * doc_lens[i] / avgdl)
            score = idf * (tf * (k1 + 1)) / denom
            scores[i] += score

    return scores
    pass