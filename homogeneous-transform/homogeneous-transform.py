import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    T , points= np.array(T) , np.array(points)
    points = np.concatenate([points, np.ones((*points.shape[:-1], 1))], axis=-1)
    ans = (T @ points.T)[:-1].T
    return ans
