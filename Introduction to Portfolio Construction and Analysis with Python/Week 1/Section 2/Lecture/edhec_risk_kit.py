# Building your own module lecture,


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #import matplotlib
import scipy.stats

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