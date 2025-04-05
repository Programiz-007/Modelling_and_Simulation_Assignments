import numpy as np
import matplotlib.pyplot as plt


r = 1      
k = 1000   
h_values = [ 0,100, 500]  
x0 = 10    
dt = 0.0001
T = 2
t_vals = np.arange(0, 15, dt)  


def dx_dt(x, h):
    return (r * x * (1 - x/k)) - h


x_range = np.linspace(0, k, 400)
plt.figure(figsize=(8, 5))
for h in h_values:
    dx_vals = dx_dt(x_range, h)
    plt.plot(x_range, dx_vals, label=f"h = {h}")

plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.xlabel("x (Population)")
plt.ylabel("dx/dt (Growth Rate)")
plt.title("Phase Plot of the Logistic Model with Harvesting")
plt.legend()
plt.grid()
plt.show()


plt.figure(figsize=(8, 5))
for h in h_values:
    x_num = np.zeros(len(t_vals))
    x_num[0] = x0

    for i in range(1, len(t_vals)):
        x_num[i] = x_num[i-1] + dt * dx_dt(x_num[i-1], h)
        # if x_num[i] < 0:  
        #     x_num[i] = 0

    plt.plot(t_vals, x_num, label=f"h = {h}")

plt.xlabel("Time (t)")
plt.ylabel("x(t) (Population)")
plt.title("Numerical Solution of the Logistic Model with Harvesting")
plt.legend()
plt.ylim(-10000,2000)
plt.grid()
plt.show()


def x_analytical(t):
    return (x0 * k * np.exp(r * t)) / (k + x0 * (np.exp(r * t) - 1))


x_analytic_vals = x_analytical(t_vals)
x_num_h0 = np.zeros(len(t_vals))
x_num_h0[0] = x0

for i in range(1, len(t_vals)):
    x_num_h0[i] = x_num_h0[i-1] + dt * dx_dt(x_num_h0[i-1], 0)


plt.figure(figsize=(8, 5))
plt.plot(t_vals, x_analytic_vals, label="Analytical Solution", color="blue")
plt.plot(t_vals, x_num_h0, label="Euler's Method", linestyle="--", color="orange")
plt.xlabel("Time (t)")
plt.ylabel("x(t)")
plt.title("Comparison of Analytical and Numerical Solutions (h = 0)")
plt.legend()
plt.grid()
plt.show()


relative_error = (np.abs(-x_analytic_vals + x_num_h0) / x_analytic_vals)

plt.figure(figsize=(8, 5))
plt.plot(t_vals, relative_error, color="red")
plt.xlabel("Time (t)")
plt.ylabel("Relative Error")
plt.title("Relative Error between Analytical and Numerical Solutions (h = 0)")
plt.grid()
plt.show()
