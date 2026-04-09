import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    p , y = np.array(p) , np.array(y)
    return 1- (2*(p*y).sum() + eps) / (p.sum() + y.sum() + eps)