import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    freq_arr = np.arange(0, d_model).reshape(1, -1) *  np.ones((seq_len, 1))

    for i in range(seq_len):
        for j in range(d_model):
            if j % 2 == 0:     
                freq_arr[i][j] = np.sin(i/base **(j / d_model) )
            else:
                freq_arr[i][j] = np.cos(i/base **((j - 1) / d_model))
    return freq_arr
    
