import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def x_t(t, k, x0, a):
    return (k * x0 * np.exp(a * t)) / (k + x0 * (np.exp(a * t) - 1))

usa_gdp=np.loadtxt(r'LAB_1\GDP\USA_GDP_Trade\US_GDP.dat')
usa_trade=np.loadtxt(r'LAB_1\GDP\USA_GDP_Trade\US_Trade.dat')

t=usa_gdp[:,0]
gdp=usa_gdp[:,1]
trade=usa_trade[:,1]

k_g=30e12
a_g=0.08
x0_g=0.555e12

k_t=10e12
a_t=0.099
x0_t=0.499995e11

gdp_th=x_t(t,k_g,x0_g,a_g)
trade_th=x_t(t,k_t,x0_t,a_t)

rel_var=(-gdp_th+gdp)/gdp_th
mean=np.mean(rel_var)
standard_dev=np.std(rel_var)
print("Mean of relative Variation for GDP",mean)
print("Standard Deviation of relative Variation for GDP",standard_dev)

rel_var=(-trade_th+trade)/trade_th
mean=np.mean(rel_var)
standard_dev=np.std(rel_var)
print("Mean of relative Variation for Trade",mean)
print("Standard Deviation of relative Variation for Trade",standard_dev)

plt.plot(t, gdp, color='blue',label='GDP')
plt.plot(t, trade, color='red',label='Trade')
plt.plot(t, gdp_th, label=r'GDP', color='black')
plt.plot(t, trade_th, label=r'Trade', color='black')
plt.yscale('log')
plt.xlabel('t (years)')
plt.ylabel('G and T growth')
plt.title('USA')
plt.legend()
plt.show()

alpha=a_g/a_t
# alpha=0.65
trade=trade**alpha
trade_th=trade_th**alpha

plt.scatter(trade,gdp,color='red',marker='+')
plt.plot(trade_th,gdp_th,color='black')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('T')
plt.ylabel('G')
plt.title('USA')
plt.show()