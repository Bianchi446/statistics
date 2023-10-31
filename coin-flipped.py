from scipy.stats import binom 
import numpy as np 

X = binom.rvs(1, 0.5, size=50)

print(X)
