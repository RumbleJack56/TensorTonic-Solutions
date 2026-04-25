import numpy as np
def average_pooling_2d(X, pool_size):
    """
    Apply 2D average pooling with non-overlapping windows.
    """
    X = np.array(X)
    
    return [
        [
            X[i:i+pool_size,j:j+pool_size].mean() 
            for j in range(0,X.shape[1],pool_size)
        ]
        for i in range(0,X.shape[0],pool_size)
    ]
    
            