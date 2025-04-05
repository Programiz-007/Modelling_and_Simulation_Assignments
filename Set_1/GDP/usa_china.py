import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def x_t(t, k, x0, a):
    return (k * x0 * np.exp(a * t)) / (k + x0 * (np.exp(a * t) - 1))

china=np.loadtxt('LAB_1\GDP\China_GDP_Trade.dat')
usa_gdp=np.loadtxt(r'LAB_1\GDP\USA_GDP_Trade\US_GDP.dat')

t=usa_gdp[:,0]
gdp_usa=usa_gdp[:,1]
gdp_china=china[:,1]

# USA
k_g=30e12
a_g=0.08
x0_g=0.555e12

gdp_th_usa=x_t(t,k_g,x0_g,a_g)

# China
k_g=80e12
a_g=0.095
x0_g=0.585e11

gdp_th_china=x_t(t,k_g,x0_g,a_g)

# Plots
plt.plot(t, gdp_usa, color='blue',label='USA')
plt.plot(t, gdp_th_usa, label=r'USA', color='blue',linestyle='--')
plt.plot(t, gdp_china, color='black',label='China')
plt.plot(t, gdp_th_china, label=r'China', color='black',linestyle='--')
plt.xlabel('t (years)')
plt.ylabel('G')
plt.yscale('log')
plt.legend()
plt.title('GDP USA and China')
plt.show()