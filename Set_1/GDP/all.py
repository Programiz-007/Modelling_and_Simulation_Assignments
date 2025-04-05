import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def x_t(t, k, x0, a):
    return (k * x0 * np.exp(a * t)) / (k + x0 * (np.exp(a * t) - 1))

t=np.arange(0,100)

# germany
k_g=4.4e12
a_g=0.11
x0_g=1.40e11
gdp_th_germany=x_t(t,k_g,x0_g,a_g)

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

# UK
k_g=3e12
a_g=0.105
x0_g=0.7e11
gdp_th_uk=x_t(t,k_g,x0_g,a_g)

# plots
plt.plot(t,gdp_th_germany,linestyle='--',linewidth=1,label='Germany')
plt.plot(t,gdp_th_japan,linestyle='--',linewidth=2,label='Japan')
plt.plot(t,gdp_th_uk,linestyle='--',linewidth=3,label='UK')
plt.plot(t,gdp_th_india,linestyle='--',color='black',label='India')
plt.legend()
plt.title('GDP of Germany, Japan, UK and India')
plt.xlabel('t (years)')
plt.ylabel('G')
plt.yscale('log')
plt.show()