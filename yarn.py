import mistat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


X = mistat.load_data('YARNSTRG')

ax = X.plot.hist(bins=5, color='white', edgecolor='black', legend=False)
ax.set_xlabel('Log yarn strength')
plt.show()

ecdf = pd.DataFrame({'Log yarn strength ' : X.sort_values(), 
                    'Fn(x)' : range(1, len(X) + 1)})

ecdf['Fn(x)'] = ecdf['Fn(x)'] / len(X)
ax = ecdf.plot(x='Log yarn strength', y='Fn(x)', color='black', 
                drawstyle='steps-post', legend=False)

ax.axhline(y=0, color='grey', linestyle='--')
ax.axhline(y=1, color='grey', linestyle='--')
ax.set_ylabel('Fn(x)')
plt.show()



