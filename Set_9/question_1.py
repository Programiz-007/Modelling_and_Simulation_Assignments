import numpy as np
import matplotlib.pyplot as plt

def euler_method(fx, fy, x0, y0, t0, t_end, dt):
    t_values = np.arange(t0, t_end, dt)
    x_values = np.zeros(len(t_values))
    y_values = np.zeros(len(t_values))
    
    x_values[0] = x0
    y_values[0] = y0
    
    for i in range(1, len(t_values)):
        x_values[i] = x_values[i-1] + dt * fx(x_values[i-1], y_values[i-1])
        y_values[i] = y_values[i-1] + dt * fy(x_values[i-1], y_values[i-1])
    
    return t_values, x_values, y_values

def plot_results(t, x, y, title):
    plt.figure(figsize=(12, 5))
    plt.plot(t, x, label='x-species')
    plt.plot(t, y, label='y-species')
    plt.xlabel('Time (t)')
    plt.ylabel('Population Density')
    plt.title(title)
    plt.legend()
    plt.show()
    
    plt.figure(figsize=(6, 6))
    plt.plot(x, y)
    plt.xlabel('x-species')
    plt.ylabel('y-species')
    plt.title('Phase Space Plot')
    plt.show()

# Given parameters
A = 0.21827
C = 0.06069
dt = 0.0001
t0, t_end = 0, 50

# Case A: B = D = 0, α = 0.05289, β = 0.00459
B, D = 0, 0
alpha, beta = 0.05289, 0.00459
x0, y0 = 0.5, 1.5

def fx1(x, y): return A*x - B*x**2 - alpha*x*y

def fy1(x, y): return C*y - D*y**2 - beta*x*y

t_values, x_values, y_values = euler_method(fx1, fy1, x0, y0, t0, t_end, dt)
plot_results(t_values, x_values, y_values, 'Case A: Competitive Exclusion')

# Case B: B = 0.017, D = 0.010, α = 0.05289, β = 0.00459, x(0) = y(0) = 0.5
B, D = 0.017, 0.010
x0, y0 = 0.5, 0.5

def fx2(x, y): return A*x - B*x**2 - alpha*x*y

def fy2(x, y): return C*y - D*y**2 - beta*x*y
t0, t_end = 0, 300
t_values, x_values, y_values = euler_method(fx2, fy2, x0, y0, t0, t_end, dt)
plot_results(t_values, x_values, y_values, 'Case B: Competition with Density Regulation')
print(f'Max x: {max(x_values)}, Max y: {max(y_values)}')

# Case C: No competition, α = β = 0, B = 0.017, D = 0.010
alpha, beta = 0, 0

def fx3(x, y): return A*x - B*x**2

def fy3(x, y): return C*y - D*y**2
t0, t_end = 0, 250
t_values, x_values, y_values = euler_method(fx3, fy3, x0, y0, t0, t_end, dt)
plot_results(t_values, x_values, y_values, 'Case C: No Competition')
