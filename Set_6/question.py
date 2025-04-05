import numpy as np
import matplotlib.pyplot as plt

def traffic(A,mu,lam,t,beta):
    return A*((mu+t**2))*(np.exp(-((lam*t-beta)**2)))

traffic_dat=np.loadtxt('SET_6/traffic_time.dat')
t=traffic_dat[:,1]
west=traffic_dat[:,2]
east=traffic_dat[:,0]

A=44
mu=8.53
lam=0.19
beta=-0.09

T_val=np.arange(-11,12,0.01)
traffic_val=traffic(A,mu,lam,T_val,beta)



plt.plot(T_val,traffic_val,label='Analytical')
plt.plot(t,west,label='Data points',linestyle='--')
plt.legend()
plt.xlabel('t')
plt.ylabel('N')
plt.title("Bimodal Distribution( Traffic due West)")
plt.show()

A=44.1
mu=10.5
lam=0.22
beta=0.24
T_val=np.arange(-11,12,0.01)
traffic_val=traffic(A,mu,lam,T_val,beta)




plt.plot(T_val,traffic_val,label='Analytical')
plt.plot(t,east,label='Data points',linestyle='--')
plt.legend()
plt.xlabel('t')
plt.ylabel('N')
plt.title("Bimodal Distribution( Traffic due East)")
plt.show()