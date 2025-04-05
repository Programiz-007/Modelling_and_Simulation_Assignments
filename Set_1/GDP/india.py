import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def x_t(t, k, x0, a):
    return (k * x0 * np.exp(a * t)) / (k + x0 * (np.exp(a * t) - 1))

india=np.loadtxt('LAB_1\GDP\India_GDP_Trade.dat')

t=india[:,0]
gdp=india[:,1]
trade=india[:,2]

k_g=6e12
a_g=0.08
x0_g=0.349e11

k_t=3e12
a_t=0.1
x0_t=0.404e10

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
plt.title('India')
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
plt.title('India')
plt.show()

def x_v(t, k, x0, a):
    return (x0 * np.exp(a * t))

t=np.arange(0,95)
gdp_forecasted=x_v(t,k_g,x0_g,a_g)

print("In 2047 India's GDP will be equal to (based on only exponential growth) = ",x_v(87,k_g,x0_g,a_g)/1e12,"Trillion US Dollars")

time=87
gdp_2047=x_v(time,k_g,x0_g,a_g)

plt.scatter(time,gdp_2047,color='black',marker='D')
plt.plot(t,gdp_forecasted,color='orange')
plt.xlabel('t')
plt.ylabel('G')
plt.show()

def t_func(x,x0_g,a_g,k_g):
    return np.log((x*(k_g-x0_g))/(x0_g*(k_g-x)))*(1/a_g)

t_4=t_func(4e12,x0_g,a_g,k_g)
t_5=t_func(5e12,x0_g,a_g,k_g)

t_4=int(t_4)+1960
t_5=int(t_5)+1960

print("Time when India's GDP to reach 4 trillion dollars",t_4)
print("Time when India's GDP to reach 5 trillion dollars",t_5)
