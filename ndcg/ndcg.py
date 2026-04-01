import math

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """
    dcg = 0
    # Write code here
    for i in range(1, min(len(relevance_scores) + 1, k+1)):
        dcg += (2 ** relevance_scores[i-1] - 1) / math.log(i + 1)

    idcg = 0
    relevance_scores_ideal = relevance_scores.sort(reverse=True) 
    for i in range(1, min(len(relevance_scores) + 1, k+1)):
        idcg += (2 ** relevance_scores[i-1] - 1) / math.log(i + 1)

    if idcg == 0:
        return 0.0

    return dcg / idcg
