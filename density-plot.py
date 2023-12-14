import mistat
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from KDEpy.bw_selection import improved_sheather_jones 

X = mistat.load_data('YARNSTRG')
X.plot.density()

h = improved_sheather_jones(X.values.reshape(-1, 1))
ax = X.plot.density(color='grey')
X.plot.density(bw_method=h, color='black', ax=ax)
ax.set_xlabel('Log yarn strength')
ax.set_ylabel(f'density(h={h: .2f})')
plt.show()
