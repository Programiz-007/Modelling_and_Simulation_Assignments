import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



net_profit=np.loadtxt('IBM\prof_ibm.dat')

t=net_profit[:,0]
profit=net_profit[:,1]

plt.plot(t,profit,label='Net Profit',color='green')
plt.xlabel('t(years)')
plt.ylabel('Net Annual Earnings(Profit)')
plt.title('Profit')
plt.legend()
plt.show()