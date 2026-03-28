import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    return np.array([p + (i==0)*(1-2*p) for i in x]) , p , p * (1-p)