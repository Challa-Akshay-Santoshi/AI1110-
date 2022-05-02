# C. Akshay Santoshi
# CS21BTECH11012

# Assignment 5

import numpy as np

# Representing outcomes for different events when dice is thrown.

# Outcomes less than 7
arr1 = np.arange(1, 7, 1)
print("Events where number is less than 7 is: ", arr1)

# Outcomes greater than 7
print("Events where number is greater than 7 do not exist")

# Outcomes multiple of 3
arr2 = np.arange(3, 7, 3)
print("Events where number is multiple of 3 is: ", arr2)

# Outcomes less than 4
arr3 = np.arange(1, 4, 1)
print("Events where number is less than 4 is: ", arr3)

# Even outcomes greater than 4
arr4 = np.arange(6, 7, 1)
print("Events where number is even and greater than 4 is: ", arr4)

# Outcomes not less than 3
arr5 = np.arange(3, 7, 1)
print("Events where number is not less than 3 is: ", arr5)