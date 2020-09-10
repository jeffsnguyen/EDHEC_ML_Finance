# Downsidelecture,


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #import matplotlib
import edhec_risk_kit as erk
import scipy.stats



def main(number_of_obs=None):

    # Call the function from edhec_risk_kit
    hfi = erk.get_hfi_returns()
    # Semi deviation
    hfi.std(ddof = 0) # average deviation from the mean

    hfi[hfi < 0].std(ddof =0)
    erk.semideviation[hfi]

    # VaR and CVaR
    # Value at Risk and Conditional Value at Risk

    # Historic VaR

    # What's value at risk at 5%: 5 percentile VaR
    np.percentile(hfi, 5, axis = 0)
    erk.var_historic(hfi)

    # Parametric VaR - Gaussian parametric
    z = norm.ppf(.05) # normal dist: return a z-score where half of the distribution lies below it
    - hfi.mean() + z*hfi.std(ddof = 0)

    # Modified Cornish - Fisher VaR
    var_list = [erk.var_gaussian(hfi), erk.var_gaussian(hfi, modified = True), erk.var_historic(hfi)]
    comparison = pd.concat(var_list)
    comparison.columns = ['Gaussian', 'Cornish-fisher', 'Historic']
    comparison.plot.bar(title = 'EDHEC Hedfe Fund Indicies: VaR')

    # Beyond Car aka. CVaR
    erk.cvar_historic(hfi)

#######################
if __name__ == '__main__':
    main()