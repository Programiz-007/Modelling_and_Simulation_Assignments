import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('IBM\groibm.dat')

def x_t(t, k, x0, a):
    return (k * x0 * np.exp(a * t)) / (k + x0 * (np.exp(a * t) - 1))

rev=data[:,0]
hsrc=data[:,1]

marker_size=20

k_R = 100000  # Constant for R
x0_R = 2.064  # Initial value for R
a_R = 0.145 # Growth rate for R

k_H = 500000 # Constant for H
x0_H = 1520  # Initial value for H
a_H = 0.09 # Growth rate for H

t=np.arange(1,94)

beta = a_R/a_H

V=1/rev - 1/k_R
U=(1/hsrc - 1/k_H)**beta

rev_values=x_t(t, k_R, x0_R, a_R)
hsrc_values=x_t(t, k_H, x0_H, a_H)

V_theoretical=(1/rev_values) - (1/k_R)
U_theoretical=((1/hsrc_values) - (1/k_H))**beta


plt.scatter(U,V,color='indigo',s=marker_size,marker='x')
plt.plot(U_theoretical,V_theoretical,color='orange')
plt.title('Correlated Growth of H and R')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('U')
plt.ylabel('V')
plt.show()











