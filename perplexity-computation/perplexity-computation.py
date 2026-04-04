import numpy as input
def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    prob_arr = np.array([prob_distributions[i][actual_tokens[i]] for i in range(len(actual_tokens))])

    cross_entropy = -np.mean(np.log(prob_arr))
    
    pp = np.exp(cross_entropy)
    return pp