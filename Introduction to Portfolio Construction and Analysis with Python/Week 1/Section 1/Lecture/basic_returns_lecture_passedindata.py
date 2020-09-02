'''
Basics of Returns lecture
'''

import numpy as np
import pandas as pd



def main():
    # Price is a sequence -> Returns can be calculated using a sequence too

    # Using numpy
    # Create a numpy array and assign price list
    prices_a = np.array([8.70,8.91,8.71])
    print(prices_a)
    returns_a = (prices_a[1:] / prices_a[:-1]) - 1
    print(returns_a)

    # Using pandas
    prices = pd.DataFrame({"BLUE": [8.70, 8.91, 8.71, 8.43, 8.73]
                              ,
                           "ORANGE": [10.66, 11.08, 10.71, 11.59, 12.11]
                           })
    print(prices)

    # Index location iloc:

    # Option 1
    # .iloc: Starting from index 1 to the end
    # .values: take the value only without the row index
    returns_b = prices.iloc[1:].values / prices.iloc[:-1].values - 1
    print(returns_b)

    # Option 2: shift
    returns_b = prices / prices.shift(1) - 1
    print(returns_b)

    # Option 3: pct_change
    returns_b = prices.pct_change()
    print(returns_b)
#######################
if __name__ == '__main__':
    main()