import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def x_t(t, k, x0, a):
    return (k * x0 * np.exp(a * t)) / (k + x0 * (np.exp(a * t) - 1))

human_rsrc = np.loadtxt('IBM\groibm.dat')

t=human_rsrc[:,2]
hsrc=human_rsrc[:,1]


k=500000
a=0.09
x0=1520

x_values = x_t(t, k, x0, a)

rel_var=(-x_values+hsrc)/x_values
mean=np.mean(rel_var)
standard_dev=np.std(rel_var)
print("Mean of relative Variation",mean)
print("Standard Deviation of relative Variation",standard_dev)

plt.scatter(t, hsrc, color='green',label='Data')
plt.plot(t, x_values, label=r'$x(t) = \frac{k x_0 e^{at}}{k + x_0 (e^{at} - 1)}$', color='blue')
plt.yscale('log')
plt.xlabel('t')
plt.ylabel('Human Resource Growth')
plt.title('Human Resource Growth')
plt.legend()
plt.show()
