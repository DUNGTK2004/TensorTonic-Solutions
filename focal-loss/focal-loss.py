import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    p = np.array(p)
    y = np.array(y)
    term_1 = (1-p) ** gamma * y * np.log(p) 
    term_2 = p ** gamma * (1 - y) * np.log(1 - p)
    f_loss = -(term_1 + term_2)

    return np.mean(f_loss)