import numpy as np
from collections import Counter
def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    preds = list(map(Counter,zip(*predictions)))
    ans = []
    for pred in preds:
        for i in sorted(pred): 
            if pred[i] == max(pred.values()):
                ans.append(i)
                break
    return ans