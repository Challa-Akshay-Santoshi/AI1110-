import numpy as np
import mpmath as mp
import scipy
import matplotlib.pyplot as plt

maxrange=50
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
randvar = np.loadtxt('triangular.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

plt.plot(x[0:(maxrange-1)].T,pdf,'o')
plt.grid() #creating the grid
plt.xlabel('$t_i$')
plt.ylabel('$p_T(t_i)$')
plt.legend(["Numerical"])

plt.savefig('../figs/triangular_pdf.pdf')
plt.savefig('../figs/triangular_pdf.eps')