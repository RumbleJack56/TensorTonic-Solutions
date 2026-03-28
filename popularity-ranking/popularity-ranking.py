import numpy as np
def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    a , b = list(map(np.array,zip(*items)))
    return ((a * b + min_votes * global_mean) / (b+min_votes)).tolist()
    