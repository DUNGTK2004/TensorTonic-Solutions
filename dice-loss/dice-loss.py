import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    # Write code here
    p = np.asarray(p, dtype=float)
    y = np.asarray(y, dtype=float)
    if p.ndim == 2:
        p = p.flatten()
        y = y.flatten()
    dice = (2 * np.sum(np.dot(p, y)) + eps) / (np.sum(p) + np.sum(y) + eps)
    dice_loss = 1 - dice
    return dice_loss