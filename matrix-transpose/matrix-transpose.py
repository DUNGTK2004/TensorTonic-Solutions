import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    arr = np.array(A)
    w, h = arr.shape
    arr_t = np.zeros((h, w))
    for i in range(len(A)):
        for j in range(len(A[i])):
            arr_t[j][i] = arr[i][j]
    return arr_t
