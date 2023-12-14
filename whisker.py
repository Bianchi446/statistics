import mistat
import numpy as np 
import  pandas as pd
import matplotlib.pyplot as plt 


X = mistat.load_data('YARNSTRG')
ax = X.plot.box(color='black')
ax.set_ylabel('Log Yarn Strength')
plt.show()
