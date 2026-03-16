import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    arr = np.array(X)
    u = np.mean(arr, axis=0)
    center = arr - u 
    if arr.ndim == 1 or arr.shape[0] == 1: 
        return None
    else:
        s = (1 / (arr.shape[0] - 1)) * center.T @ center
        return s