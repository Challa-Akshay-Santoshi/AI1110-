# C. Akshay Santoshi
# CS21BTECH11012

# Assignment-3

#Plotting Frequency Polygon

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the data from excel sheet
df= pd.read_excel(r'C:\Users\aksha\Documents\Book1.xlsx').to_numpy()

# Arrays to store the data of different columns
intervals = df[:, 0]
TeamA = df[:, 1]
TeamB = df[:, 2]

# To split the intervals column into two new columns
limits = np.array([i.split("-") for i in intervals], dtype="float64")
Lower_Limit = limits[:, 0]
Upper_Limit = limits[:, 1]

# Frequency polygon requires the midpoint of the class intervals
Midpoint = (Lower_Limit + Upper_Limit) / 2

# To touch the x-axis
first_diff = Midpoint[1] - Midpoint[0]
last_diff = Midpoint[-1] - Midpoint[-2]
first = Midpoint[0] - first_diff
last = Midpoint[-1] + last_diff

# Adding the y-values where it touches y-axis
TeamA = np.concatenate(([0], TeamA, [0]))
TeamB = np.concatenate(([0], TeamB, [0]))
midpoints = np.concatenate(([first], Midpoint, [last]))

#Plotting the frequency polygon
plt.xlabel("Number of Balls")
plt.ylabel("Runs Scored")
plt.plot(midpoints, TeamA, '-o', label="TeamA")
plt.plot(midpoints, TeamB, '-o', label="TeamB")
plt.legend()
plt.show()