# Deviation from Normality lecture,


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #import matplotlib
import edhec_risk_kit as erk
import scipy.stats



def main(number_of_obs=None):

    # Call the function from edhec_risk_kit
    hfi = erk.get_hfi_returns()
    print(hfi.head())

    # Measure skewness
    print(pd.concat([hfi.mean(), hfi.median(), hfi.mean() > hfi.median()], axis = 'columns'))
    erk.skewness(hfi).sort_values()

    # Comparing built in method (scipy) with our own function
    scipy.stats.skew(hfi)
    erk.skewness(hfi)

    #hfi.shape()
    normal_rets = np.random.normal(0, .15, size = (263, 1)) # Random generated returns in the form of 263x1 array
    erk.skewness(normal_rets)


    # Measure kurtosis
    erk.kurtosis(normal_rets)
    scipy.stats.kurtosis(normal_rets) # Excess kurtosis

    # Jarque Bera Test
    scipy.stats.jarque_bera(normal_rets)
    scipy.stats.jarque_bera(hfi)
    erk.is_normal(normal_rets)
    erk.is_normal(hfi)
    hfi.aggregate(erk.is_normal) # Take the given function, apply it on every col and give result

    ffme = erk.get_ffme_returns()
    erk.skewness(ffme)
    erk.kurtosis(ffme)

    erk.is_normal(ffme)
    ffme.aggregate(erk.is_normal)

#######################
if __name__ == '__main__':
    main()