import mistat
import matplotlib.pyplot as plt 

steelrod = mistat.load_data("STEELROD")

# Create a scatterplot 

ax = steelrod.plot(y = 'STEELROD', style='.', color='black')
ax.set_xlabel('Index')
ax.set_ylabel('Steel Rod Length') 
plt.show()


