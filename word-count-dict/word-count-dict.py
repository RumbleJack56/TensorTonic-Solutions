from collections import Counter
def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    return dict(Counter(w for sen in sentences for w in sen))
    