import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x =  np.asarray(x)
    if x.ndim == 2:
        mean = np.mean(x, axis=0, keepdims=True)
        var = np.std(x, axis=0, keepdims=True) ** 2
    if x.ndim == 4:
        mean = np.mean(x, axis=(0, 2, 3), keepdims=True)
        var = np.std(x, axis=(0, 2, 3), keepdims=True) ** 2
        x_shape = x.shape
        gamma = np.array(gamma).reshape(1, x_shape[1], 1, 1)
        beta = np.array(beta).reshape(1, x_shape[1], 1, 1)
        
    x_norm =(x - mean) / np.sqrt(var + eps)
    shift = gamma * x_norm + beta
    return shift
    