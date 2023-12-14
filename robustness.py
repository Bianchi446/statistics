import mistat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.stats import trim_mean 

Oelect = mistat.load_data('OELECT')

def mySummary(x, trim=0):
    """ Returns summary information for list x 

    The optional argument trim can be used to calculate a trimmed mean """

    X = pd.Series(x)

    quantiles = list(x.quantile(q=[0, 0.25, 0.5, 0.75, 1.0]))
    trimmed_mean = trim_mean(x, trim) 

    """ Return summary information as pandas series """

    return pd.Series({

        'Min' : quantiles[0],
        'Q1' : quantiles[1],
        'Median' : quantiles[2],
        'Mean' : trimmed_mean,
        'Q3' : quantiles[3],
        'Max' : quantiles[4],
        'SD' : x.std(),
        'IQR' : quantiles[3] - quantiles[1]
        })


# Sort and reset the index 
OutVolt = Oelect.sort_values(ignore_index=True)

OutVolt[98] = 2289.86

print(pd.DataFrame({
    'untrimmed' : mySummary(OutVolt),
    'trimmed' : mySummary(OutVolt, trim=0.05),
}))



