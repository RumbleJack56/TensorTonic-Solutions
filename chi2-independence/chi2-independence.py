import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    C = np.array(C)
    ans = (C.sum(axis=1,keepdims=True) @ C.sum(axis=0,keepdims=True))/C.sum()
    return ((ans - C)**2 / ans).sum(), ans