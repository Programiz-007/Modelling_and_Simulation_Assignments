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
    plt.plot(t, x, label='Prey (x)')
    plt.plot(t, y, label='Predator (y)')
    plt.xlabel('Time (t)')
    plt.ylabel('Population Density')
    plt.title(title)
    plt.legend()
    plt.show()
    
    plt.figure(figsize=(6, 6))
    plt.plot(x, y)
    plt.xlabel('Prey (x)')
    plt.ylabel('Predator (y)')
    plt.title('Phase Space Plot')
    plt.show()

# Given parameters
A = 1.0
B = 0.01
C = 0.5
D = 0.005
dt = 0.0001
t0, t_end = 0,50

# Case A: No human interference (ε = 0), x(0) = 200, y(0) = 80
epsilon = 0
x0, y0 = 200, 80

def fx1(x, y): return A*x - B*x*y - epsilon*x

def fy1(x, y): return -C*y + D*x*y - epsilon*y

t_values, x_values, y_values = euler_method(fx1, fy1, x0, y0, t0, t_end, dt)
plot_results(t_values, x_values, y_values, 'Case A: Predator-Prey Model without Human Interference')
print(f'Max y (without interference): {max(y_values)}')

# Case B: With human interference (ε = 0.1)
epsilon = 0.1

t_values, x_values, y_values = euler_method(fx1, fy1, x0, y0, t0, t_end, dt)
plot_results(t_values, x_values, y_values, 'Case B: Predator-Prey Model with Human Interference')
print(f'Max y (with interference): {max(y_values)}')

# Case C: No predator (y0 = 0), ε = 0
x0, y0 = 200, 0

def fx2(x, _): return A*x - epsilon*x

t_values, x_values, _ = euler_method(fx2, lambda x, y: 0, x0, y0, t0, t_end, dt)
plt.figure(figsize=(12, 5))
plt.plot(t_values, np.log(x_values), label='Log Prey Population')
plt.xlabel('Time (t)')
plt.ylabel('Log Population')
plt.title('Case C: Logarithm of Prey Population without Predators')
plt.legend()
plt.show()

# Case D: No prey (x0 = 0), ε = 0
y0 = 80

def fy3(_, y): return -C*y

t_values, _, y_values = euler_method(lambda x, y: 0, fy3, x0, y0, t0, t_end, dt)
plt.figure(figsize=(12, 5))
plt.plot(t_values, np.log(y_values), label='Log Predator Population')
plt.xlabel('Time (t)')
plt.ylabel('Log Population')
plt.title('Case D: Logarithm of Predator Population without Prey')
plt.legend()
plt.show()
