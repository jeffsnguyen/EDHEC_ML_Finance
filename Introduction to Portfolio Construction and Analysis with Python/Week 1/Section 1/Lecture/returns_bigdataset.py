'''
Basics of Returns lecture, with sample daat
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #import matplotlib



def main(number_of_obs=None):
    # Price is a sequence -> Returns can be calculated using a sequence too

    returns = pd.read_csv('Portfolios_Formed_on_ME_monthly_EW.csv',
                          header = 0, index_col = 0, parse_dates = True,
                          na_values = -99.99)
    print(returns.head())
    columns = ['Lo 10', 'Hi 10'] # Extract columns
    returns = returns[columns]
    returns = returns / 100 # Use raw .1 returns instead of 10%, so divide by 100
    returns.columns = ['Small Cap', 'Large Cap']

    #returns.plot.line()
    #plt.show()

    annualized_vol = returns.std()*np.sqrt(12)
    n_months = returns.shape[0]
    returns_per_month = (returns + 1).prod()**(1/n_months) - 1
    print(returns_per_month)

    annualized_return = (returns_per_month + 1)**12 - 1
    print(annualized_return)

    annualized_return = (returns + 1).prod()**(12/n_months) - 1

    rf_rate = 0.03
    excess_return = annualized_return - rf_rate
    sharpe_ratio = excess_return / annualized_vol
    print(sharpe_ratio)

'''
    returns = prices.pct_change()
    print(returns)

    returns = returns.dropna() # drop NA from data
    print(returns)

    #prices.plot()
    #plt.show() # specify for the plot to show

    #returns.plot.bar() # bar plot
    #plt.show()

    stdev = returns.std

    mean = returns.mean

    # Calculating volatility
    number_of_obs = returns.shape[0] #shape gives back # row and col as a tuple
    deviations = returns - returns.mean()
    squared_deviations = deviations**2
    variance = squared_deviations.sum() / (number_of_obs -1)
    volatility = np.sqrt(variance)
    print(volatility)
    print(returns.std)

    # Calculating annualized volatility
    annual_vol = returns.std() * np.sqrt(12)
    print(annual_vol)

'''
#######################
if __name__ == '__main__':
    main()