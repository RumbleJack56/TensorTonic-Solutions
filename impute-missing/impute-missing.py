import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    fill = {'mean': np.nanmean, 'median': np.nanmedian}[strategy](X, axis=0, keepdims=True)
    fill = np.where(np.isnan(fill), 0, fill)
    return np.where(np.isnan(X), fill, X)

    