import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.array(x)
    if rng: sampling = rng.random(x.shape) > p
    else: sampling = np.random.random(x.shape) > p
    sampling = sampling.astype(np.float64) / (1-p)
    return x * sampling , sampling
    