import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm 


# Create a list of values

x = [math.sin(x * 2 * math.pi / 1000) for x in range (1, 1000)]

# Add the distribution over the list 

x = [xi + norm.rvs(loc=0, scale=0.05) for xi in x]

ax = pd.Series(x).plot(style='.', color='black')
ax.set_ylabel('Values')
ax.axhline(y=0, linestyle='--', color='darkgray')
plt.show()
