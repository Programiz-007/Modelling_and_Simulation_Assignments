import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def x_t(t, k, x0, a):
    return (k * x0 * np.exp(a * t)) / (k + x0 * (np.exp(a * t) - 1))

india=np.loadtxt('LAB_1\GDP\India_GDP_Trade.dat')
japan=np.loadtxt('LAB_1\GDP\Japan_GDP_Trade.dat')

t=india[:,0]
gdp_india=india[:,1]     
gdp_japan=japan[:,1]

# India
k_g=6e12
a_g=0.08
x0_g=0.349e11
gdp_th_india=x_t(t,k_g,x0_g,a_g)

# Japan
k_g=5.2e12
a_g=0.175
x0_g=0.4e11
gdp_th_japan=x_t(t,k_g,x0_g,a_g)

# Plots
plt.plot(t, gdp_india, color='blue',label='India')
plt.plot(t, gdp_th_india, label=r'India', color='blue',linestyle='--')
plt.plot(t, gdp_japan, color='black',label='Japan')
plt.plot(t, gdp_th_japan, label=r'Japan', color='black',linestyle='--')
plt.xlabel('t (years)')
plt.ylabel('G')
plt.yscale('log')
plt.legend()
plt.title('GDP India and Japan')
plt.show()