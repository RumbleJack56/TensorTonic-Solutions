import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    x = np.array(x)
    return np.vectorize(lambda qu: np.percentile(x,qu))(q)
    