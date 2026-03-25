import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    v = np.array(v)
    w = np.array(w)

    eps = 1e-10

    norm_v = np.linalg.norm(v)
    norm_w = np.linalg.norm(w)
    if norm_v < eps or norm_w < eps:
        return np.nan
        
    dot = np.dot(v, w)
    cos = dot / (norm_v * norm_w)
    
    return np.arccos(np.clip(cos, -1.0, 1.0))
