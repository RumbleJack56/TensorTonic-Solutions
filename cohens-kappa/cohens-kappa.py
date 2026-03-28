from collections import Counter
def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    p0 = sum(a==b for a,b in zip(rater1,rater2))/len(rater1)
    r1 , r2 = Counter(rater1) , Counter(rater2)
    pe = sum(r1.get(elem,0) * r2.get(elem,0) for elem in r1 | r2)/len(rater1)/len(rater1)
    return ((p0-pe)/(1-pe)) if pe!=1 else 1
    