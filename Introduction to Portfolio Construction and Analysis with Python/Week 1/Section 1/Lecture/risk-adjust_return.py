'''
Basics of Returns lecture, with sample daat
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #import matplotlib



def main(number_of_obs=None):
    # Price is a sequence -> Returns can be calculated using a sequence too

    prices = pd.read_csv('sample_prices.csv')
    print(prices)

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


#######################
if __name__ == '__main__':
    main()