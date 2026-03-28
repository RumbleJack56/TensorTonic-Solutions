def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    recommended = set(recommended[:k])
    relevant = set(relevant)
    return [len(recommended & relevant)/k , len(recommended & relevant)/len(relevant)]