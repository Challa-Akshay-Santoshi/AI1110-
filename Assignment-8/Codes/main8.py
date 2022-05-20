# C. Akshay Santoshi
# CS21BTECH11012

import pandas as pd
import math
 
# Reads the data from excel and prints it.
df= pd.read_excel(r'C:\Users\aksha\Desktop\Book1.xlsx')
print(df)

# To find mean
df["Prob"] = df["Sum"] * df["No"]
print(df)
RV = list(df['Prob'])
print(RV)
sigma_RV = sum(RV)

Mean = sigma_RV/36
 
#To find Variance
df["SqNo"] = df["Sum"] * df["Sum"]
df["ProbSq"] = df["SqNo"] * df["No"]
SqRV = list(df['ProbSq'])
sigma2_RV = sum(SqRV)

SqSum = sigma2_RV/36

Var = SqSum - (Mean*Mean)

print(f'Variance is ', Var)

# To find Standard Deviation
print(f'Standard Deviation is ', math.sqrt(Var))