# C. Akshay Santoshi
# CS21BTECH11012

# Probability Mass Distribution

from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

# A die is thrown 6 times and success is 'getting an odd number'
n = 6
p = 0.5

# PMF Values
rv = binom(n,p)
x = np.arange(0,7,1)
y = rv.pmf(x)

# Plotting the graph
plt.plot(x, y, 'ro')
plt.vlines(x,0,y,colors = 'k', label = 'Probability')
plt.legend()
plt.show()