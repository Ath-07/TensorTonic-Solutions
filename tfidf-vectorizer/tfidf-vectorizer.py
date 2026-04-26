import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    # Write code here
    if not documents:
        return np.zeros((0, 0)), []

    tokenized_docs = [doc.lower().split() for doc in documents]

    vocab = sorted(set(token for doc in tokenized_docs for token in doc))
    vocab_index = {word: i for i, word in enumerate(vocab)}

    n_docs = len(documents)
    n_vocab = len(vocab)

    if n_vocab == 0:
        return np.zeros((n_docs, 0)), []

    df = Counter()
    for doc in tokenized_docs:
        unique_terms = set(doc)
        for term in unique_terms:
            df[term] += 1

    idf = np.zeros(n_vocab)
    for term, idx in vocab_index.items():
        idf[idx] = math.log(n_docs / df[term])

    tfidf_matrix = np.zeros((n_docs, n_vocab))

    for doc_idx, doc in enumerate(tokenized_docs):
        if not doc:
            continue
        
        term_counts = Counter(doc)
        total_terms = len(doc)
        
        for term, count in term_counts.items():
            if term in vocab_index:
                idx = vocab_index[term]
                tf = count / total_terms
                tfidf_matrix[doc_idx, idx] = tf * idf[idx]

    return tfidf_matrix, vocab
    pass