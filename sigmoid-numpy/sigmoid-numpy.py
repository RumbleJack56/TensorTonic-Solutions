import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    if not isinstance(x,np.ndarray): x = np.array(x)
    return np.pow(np.ones_like(x)+np.exp(-x),-1)