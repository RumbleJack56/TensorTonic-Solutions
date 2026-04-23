import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    # Write code here
    if len(np.array(x).shape) not in {3,4}: raise ValueError
    return np.mean(x,axis=(-1,-2))