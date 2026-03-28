import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if abs(1-sum(p)) > 1e-6: raise ValueError
    return np.array(x).T @ np.array(p)
