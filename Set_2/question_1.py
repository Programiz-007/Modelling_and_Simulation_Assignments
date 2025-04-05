import numpy as np
import matplotlib.pyplot as plt

def concentration(C0,Cin,F,V,t):
    return Cin - ((Cin-C0)*np.exp((-F*t)/V))

def time(Cin,C0,C,F,V):
    return (V/F)*np.log((Cin-C0)/(Cin-C))

C0=10
Cin=3
F=5e8
V=1e12
t=np.arange(0,10000)

conc_values=concentration(C0,Cin,F,V,t)
plt.plot(t,conc_values,label='Conc. of Pollution')
plt.title('Lake Pollution Model')
plt.xlabel('Time (days)')
plt.ylabel('Concentration of Pollution')
plt.legend()
plt.show()

time_taken=time(Cin,C0,0.5*C0,F,V)
print("Time taken for C to become 0.5*C0: ",time_taken , "days")

Cin=0

conc_values=concentration(C0,Cin,F,V,t)
plt.plot(t,conc_values,label='Conc. of Pollution',color='green')
plt.title('Lake Pollution Model(Cin=0)')
plt.legend()
plt.xlabel('Time (days)')
plt.ylabel('Concentration of Pollution')
plt.show()

time_taken=time(Cin,C0,0.5*C0,F,V)
print("Time taken for C to become 0.5*C0 (Cin=0) : ",time_taken, "days")