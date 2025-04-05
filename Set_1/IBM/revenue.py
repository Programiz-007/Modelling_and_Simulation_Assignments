import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def x_t(t, k, x0, a):
    return (k * x0 * np.exp(a * t)) / (k + x0 * (np.exp(a * t) - 1))

revenue = np.loadtxt('IBM\groibm.dat')

rev=revenue[:,0]
t=revenue[:,2]


k=100000
a=0.145
x0=2.064

x_values = x_t(t, k, x0, a)

rel_var=(-x_values+rev)/x_values
mean=np.mean(rel_var)
standard_dev=np.std(rel_var)
print("Mean of relative Variation",mean)
print("Standard Deviation of relative Variation",standard_dev)

plt.scatter(t, rev, color='green',label='Data')
plt.plot(t, x_values, label=r'$x(t) = \frac{k x_0 e^{at}}{k + x_0 (e^{at} - 1)}$', color='blue')
plt.yscale('log')
plt.xlabel('t')
plt.ylabel('Annual Revenue(million USD)')
plt.title('Annual Revenue')
plt.legend()
plt.show()
