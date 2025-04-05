import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def x_t(t, k, x0, a):
    return (k * x0 * np.exp(a * t)) / (k + x0 * (np.exp(a * t) - 1))

uk=np.loadtxt(r'LAB_1\GDP\UK_GDP_Trade.dat')
germany=np.loadtxt('LAB_1\GDP\Germany_GDP_Trade.dat')

t_g=germany[:,0]
t_g=t_g+10
t_u=uk[:,0]
t_u_temp=np.arange(-10,50)

gdp_germany=germany[:,1]
gdp_uk=uk[:,1]

# germany
k_g=4.4e12
a_g=0.11
x0_g=1.40e11
gdp_th_germany=x_t(t_u_temp,k_g,x0_g,a_g)
# UK
k_g=3e12
a_g=0.105
x0_g=0.7e11
gdp_th_uk=x_t(t_u,k_g,x0_g,a_g)

t_u_temp=t_u_temp+10
# Plots
plt.plot(t_g, gdp_germany, color='blue',label='Germany')
plt.plot(t_u_temp, gdp_th_germany, label=r'Germany', color='blue',linestyle='--')
plt.plot(t_u, gdp_uk, color='black',label='UK')
plt.plot(t_u, gdp_th_uk, label=r'UK', color='black',linestyle='--')
plt.xlabel('t (years)')
plt.ylabel('G')
plt.ylim(7.5e10)
plt.yscale('log')
plt.legend()
plt.title('GDP of Germany and UK')
plt.show()