import numpy as np 

def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    X = np.array(X)
    I = np.identity(X.shape[1])
    weight = np.linalg.inv(X.T@X + lam * I) @ X.T @ y
    return weight