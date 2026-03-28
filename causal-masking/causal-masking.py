import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    """
    scores: np.ndarray with shape (..., T, T)
    mask_value: float used to mask future positions (e.g., -1e9)
    Return: masked scores (same shape, dtype=float)
    """
    mask = np.full_like(scores, fill_value=mask_value)
    n = scores.shape[-1]
    for i in range(n):
        mask[... , i:n , i] = scores[... , i:n , i]
    return mask
    
    