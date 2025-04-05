import numpy as np
import matplotlib.pyplot as plt


a = 0.03  
b = 3e-12  
k = a / b 
x0 = 3e9  
t = np.linspace(0, 200, 500) 


x_t = (x0 * k * np.exp(a * t)) / (k + x0 * (np.exp(a * t) - 1))


plt.figure(figsize=(10, 6))
plt.plot(t, x_t, label='Analytical Solution', color='blue')
plt.axhline(y=k, color='r', linestyle='--', label='Carrying Capacity (10 billion)')
plt.xlabel('Time (years)')
plt.ylabel('Population')
plt.title('World Population Growth Prediction')
plt.legend()
plt.grid(True)
plt.show()



# Euler's method 
dt = 0.01  
t_num = np.arange(0, 300, dt) 
x_num = np.zeros(len(t_num))  
x_num[0] = x0  


for i in range(1, len(t_num)):
    x_num[i] = x_num[i-1] + dt * (a * x_num[i-1] - b * x_num[i-1]**2)


plt.figure(figsize=(10, 6))
plt.plot(t, x_t, label='Analytical Solution', color='blue')
plt.plot(t_num, x_num, label="Euler's Method Solution", color='orange', linestyle='--')
plt.axhline(y=k, color='r', linestyle='--', label='Carrying Capacity (10 billion)')
plt.xlabel('Time (years)')
plt.ylabel('Population')
plt.title('Comparison of Analytical and Numerical Solutions')
plt.legend()
plt.grid(True)
plt.show()



x_t_num = (x0 * k * np.exp(a * t_num)) / (k + x0 * (np.exp(a * t_num) - 1))


relative_error = (np.abs(-x_t_num + x_num) / x_t_num)



plt.figure(figsize=(10, 6))
plt.plot(t_num, relative_error, color='green')
plt.xlabel('Time (years)')
plt.ylabel('Relative Error')
plt.title('Relative Error between Analytical and Numerical Solutions')
plt.grid(True)
plt.show()

