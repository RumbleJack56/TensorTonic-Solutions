import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    if len(x.shape)<3: raise ValueError
    return x.sum(axis=(-2,-1))/np.multiply(*x.shape[-2:])