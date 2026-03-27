import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x =  np.asarray(x)
    if x.ndim == 2:
        axis = 0
        reshape = None
    else:
        axis = (0, 2, 3)
        reshape = (1, x.shape[1], 1, 1)

    u = np.mean(x, axis=axis, keepdims=True)
    var = np.var(x, axis=axis, keepdims=True)

    x_norm = (x - u) / np.sqrt(var + eps)
    if reshape != None:
        gamma = np.array(gamma).reshape(reshape)
        beta  = np.array(beta).reshape(reshape)

    shift = gamma * x_norm + beta
    return shift
    