import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    
    d = 0
    if len(x) != len(y):
        raise ValueError
    for i in range(len(x)):
        d += (x[i] - y[i]) ** 2
    d = np.sqrt(d)
    return d