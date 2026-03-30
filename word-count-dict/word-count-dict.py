def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    word_freq = {}
    n_seq = len(sentences)
    for idx, seq in enumerate(sentences):
        for word in seq:
            if word not in word_freq.keys():
                word_freq[word] = 1
            else:
                word_freq[word] += 1
    return word_freq
        