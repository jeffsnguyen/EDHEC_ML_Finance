'''
Basics of Returns lecture, with sample daat
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #import matplotlib



def main():
    # Price is a sequence -> Returns can be calculated using a sequence too

    prices = pd.read_csv('sample_prices.csv')
    print(prices)

    returns = prices.pct_change()
    print(returns)


    #prices.plot()
    #plt.show() # specify for the plot to show

    #returns.plot.bar() # bar plot
    #plt.show()

    stdev = returns.std
    print(stdev)

    mean = returns.mean
    print(mean)

    # Calculating compound returns
    # Option 1
    compound_returns  = np.prod(returns + 1) - 1 # numpy vector multiplication
    print(compound_returns)

    # Option 2
    compound_returns = (returns + 1).prod() - 1
    print(compound_returns)

    ## Annualization
    rm = 0.01 # Monthly returns
    annual_rm = (1 + rm ) ** 12 - 1
    print(annual_rm)


#######################
if __name__ == '__main__':
    main()