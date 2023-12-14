import mistat
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

cyclt = mistat.load_data('CYCLT')

print(cyclt.quantile(q=[0, 0.25, 0.5, 0.75, 1.0]))

