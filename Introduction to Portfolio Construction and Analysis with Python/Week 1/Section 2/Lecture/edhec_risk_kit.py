# Building your own module lecture,


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #import matplotlib
import scipy.stats
from scipy.stats import norm

# Drawdown function
def drawdown(return_series: pd.Series):
    # Takes a time series of asset returns
    # Compute and returns a DataFrame that contains:
    # wealth_index, previous_peak, drawdown

    wealth_index = 1000 * (1 + return_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks) / previous_peaks

    return pd.DataFrame({
        'Wealth': wealth_index,
        'Peaks': previous_peaks,
        'Drawdowns': drawdowns
    })

# Get Farma French market equity base returns
def get_ffme_returns():
    # Load the Farma French data set for the returns of the Top and Bottom Deciles by market cap
    me_m = pd.read_csv('Portfolios_Formed_on_ME_monthly_EW.csv', header = 0, index_col = 0, na_values = -99.99)
    rets = me_m['Lo 10', 'Hi 10']
    rets = rets/100
    rets.index = pd.to_datetime(rets.index, format = '%Y%m').to_period('M')
    return rets

def get_hfi_returns():
    # Load and format EDHEC Hedge Fund Index Returns
    hfi = pd.read_csv('edhec-hedgefundindices.csv', header = 0, index_col = 0, parse_dates = True)
    hfi  = hfi/100
    hfi.index = hfi.index.to_period('M')
    return hfi

# Semi deviation
# Returns the semideviation aka negative semideviation of r
# r must be a Series or DataFrame
def semideviation(r):
    is_negative = r <0
    return r[is_negative].std[ddof = 0]

# Skewness of a set of returns
# Formula: S(R) = E[R-E(R))^3] / stdev_R^3
# Expected value of R is mean of R
def skewness(r):
    # Alternative to scipy.stats.skew()
    # Computes the skewness of the supplied Series or DataFrame
    # Returns a float or a Series
    demeaned_r = r - r.mean()

    # Use the population standard deviation, so set degree of freedom dof = 0
    sigma_r = r.std(ddof = 0) # Volatility
    exp = (demeaned_r**3).mean()
    return exp/sigma_r**3

# Kurtosis of a set of returns
# Formula: K(R) = E[R-E(R))^4] / stdev_R^4
# Expected value of R is mean of R
def kurtosis(r):
    # Alternative to scipy.stats.kurtosis()
    # Computes the kurtosis of the supplied Series or DataFrame
    # Returns a float or a Series
    demeaned_r = r - r.mean()

    # Use the population standard deviation, so set degree of freedom dof = 0
    sigma_r = r.std(ddof = 0) # Volatility
    exp = (demeaned_r**4).mean()
    return exp/sigma_r**4

def is_normal(r, level = .01): # 1% level of confidence
    # Applies the Jarque-Bera test to determine if a Series is normal or not
    # Test is applied at the 1% level by default
    # Returns True if the hypothesis of normality is accepted, False otherwise
    statistic, p_value = scipy.stats.jarque_bera(r)
    return p_value > level

# VaR Historic
def var_historic(r, level = 5):
    if isinstance(r, pd.DataFrame): # if r is a DataFrame, return true, else false
        return r.aggregate(var_historic, level = level) # call var_historic on every column of the data frame
                                                        # => become a series, move to elif below
    elif isinstance(r, pd.Series):
        return np.percentile(r, level)
    else:
        raise TypeError('Expected r to be Series or DataFrame')

# Return the Parametric Gaussian VaR of a Series or Data Frame
def var_gaussian(r, level = 5, modified = False):
    # compute the z-score and assuming it was Gaussian
    z = norm.ppf(level/100)
    if modified:
        # Modify the z-score based on observed skewness and kurtosis
        s = skewness(r)
        k = kurtosis(r)
        z = (z + (z**2 - 1)/6 + (z**3 - 3*z)*(k-3)/24 - (2*z**3 - 5*z)(s**2)/36)
    return -(r.mean() + z*r.std(ddof = 0))


# Compute the Conditional VaR of Series or Data Frame
def cvar_historic(r, level = 5)
    if isinstance(r, pd.Series):
        is_beyond = r <= -var_historic(r, level = level) # find all returns that are less than historic var
        return -r[is_beyond].mean() # get conditional mean
    elif isinstance(r, pd.DataFrame):
        return r.aggregate(cvar_historic, level = level)
    else:
        raise TypeError('Expected r to be a Series or DataFrame')