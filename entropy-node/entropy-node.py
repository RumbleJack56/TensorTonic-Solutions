import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    counts = np.unique(y, return_counts=True)[1] / len(y)
    return -np.sum(counts.T @ np.log2(counts))