import numpy as np

def entropy_node(y):
    y = np.asarray(y)
    
    _, counts = np.unique(y, return_counts=True)
    probs = counts / counts.sum()
    
    probs = probs[probs > 0]
    return -np.sum(probs * np.log2(probs))