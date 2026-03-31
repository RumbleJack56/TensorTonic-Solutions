import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v = np.array(v).astype(np.float64)
    return np.divide(v, (norm:=np.linalg.norm(v,axis=-1,keepdims=True)), out=np.zeros_like(v), where=norm != 0)