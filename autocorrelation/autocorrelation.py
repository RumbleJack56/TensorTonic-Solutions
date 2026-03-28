import numpy as np
def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    n = len(series)
    series = np.array(series)
    if (series==series[0]).astype(int).sum() == n: return [1] + [0]*max_lag
    ans = []
    for i in range(max_lag+1):
        ans.append(((series[:n-i] - series.mean()) * (series[i:] - series.mean())).sum() / series.var()/n) 
    return ans