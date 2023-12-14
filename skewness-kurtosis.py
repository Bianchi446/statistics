import mistat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.stats import skew, kurtosis


X = mistat.load_data('YARNSTRG')
print(f'Skewness {X.skew():.4f}') # Computes the skewness
print(f'Kurtosis {X.kurtosis():.4f}') # Computes the kurtosis
from scipy.stats import skew, kurtosis
print(f'Skewness {skew(X):.4f}') # Computes the skewness
print(f'Kurtosis {kurtosis(X):.4f}') # Computes the kurtosis
