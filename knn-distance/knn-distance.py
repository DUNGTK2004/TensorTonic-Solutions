import numpy as np

def knn_distance(X_train, X_test, k):
    """
    Compute pairwise distances and return k nearest neighbor indices.
    """
    X_train = np.asarray(X_train)
    X_test = np.asarray(X_test)

    if len(X_test) == 0:
        return np.empty((0, k), dtype=int)

    k_nearest = []

    for i in range(len(X_test)):
        distances = []

        for idx in range(len(X_train)):
            dist = np.sqrt(np.sum((X_train[idx] - X_test[i]) ** 2))
            distances.append(dist)

        sorted_keys = list(np.argsort(distances)[:k])

        if len(distances) < k:
            for _ in range(k - len(distances)):
                sorted_keys.append(-1)

        k_nearest.append(sorted_keys)

    return np.array(k_nearest)