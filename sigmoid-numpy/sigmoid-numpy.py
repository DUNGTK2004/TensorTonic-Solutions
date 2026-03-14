import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    arr = np.array(x)
    denominator = 1 + np.exp(-arr)
    sig = np.divide(1, denominator)
    return sig