import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v = np.asarray(v, dtype=float)

    if v.ndim == 1:
        norm = np.linalg.norm(v)
        if norm == 0:
            return v
        return v / norm

    else:
        norms = np.linalg.norm(v, axis=1, keepdims=True)
        norms[norms == 0] = 1
        return v / norms