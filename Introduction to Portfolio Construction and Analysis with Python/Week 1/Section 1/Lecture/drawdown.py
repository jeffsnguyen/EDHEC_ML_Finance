#Drawdown lecture, with sample daat


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


def main():
    # Price is a sequence -> Returns can be calculated using a sequence too

    me_m = pd.read_csv('Portfolios_Formed_on_ME_monthly_EW.csv',
                          header = 0, index_col = 0, parse_dates = True,
                          na_values = -99.99)
    rets = me_m[['Lo 10', 'Hi 10']]
    rets.columns = ['Small Cap', 'Large Cap']
    rets = rets / 100 # Use raw .1 returns instead of 10%, so divide by 100

    #rets.plot.line()
    #plt.show()

    rets.index = pd.to_datetime(rets.index, format = "%Y%m")
    rets.index = rets.index.to_period('M')

    # Computing drawdown
    # 1. Compute a wealth index
    # 2. Compute previous peaks
    # 3. Compute drawdown which is the wealth value as a percentage of prev peak



    print(drawdown(rets['Large Cap'])[['Wealth', 'Peaks']].head())

    #drawdown(rets[:'1950']['Large Cap'])[['Wealth', 'Peaks']].plot.line()
    #plt.show()

    print(drawdown(rets['Large Cap'])['Drawdowns'].min())
    print(drawdown(rets['Large Cap'])['Drawdowns'].idxmin())

#######################
if __name__ == '__main__':
    main()