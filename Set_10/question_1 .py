import numpy as np
import matplotlib.pyplot as plt

def euler_method(fx, fy, fz, x0, y0, z0, t0, t_end, dt):
    t_values = np.arange(t0, t_end, dt)
    x_values = np.zeros(len(t_values))
    y_values = np.zeros(len(t_values))
    z_values = np.zeros(len(t_values))
    
    x_values[0] = x0
    y_values[0] = y0
    z_values[0] = z0
    
    for i in range(1, len(t_values)):
        x_values[i] = x_values[i-1] + dt * fx(x_values[i-1], y_values[i-1])
        y_values[i] = y_values[i-1] + dt * fy(x_values[i-1], y_values[i-1])
        z_values[i] = z_values[i-1] + dt * fz(x_values[i-1])
    
    return t_values, x_values, y_values, z_values

def plot_results(t, x, y, z, title):
    plt.figure(figsize=(12, 5))
    plt.plot(t, x, label='Infected (x)')
    plt.plot(t, y, label='Susceptible (y)')
    plt.xlabel('Time (days)')
    plt.ylabel('Population')
    plt.title(title)
    plt.legend()
    plt.show()
    
    plt.figure(figsize=(12, 5))
    plt.plot(t, x, label='Infected (x)')
    plt.plot(t, y, label='Susceptible (y)')
    plt.yscale('log')
    plt.xlabel('Time (days)')
    plt.ylabel('Log Population')
    plt.title(title + ' (Log Scale)')
    plt.legend()
    plt.show()
    
    plt.figure(figsize=(12, 5))
    plt.plot(t, z, label='Recovered (z)')
    plt.xlabel('Time (days)')
    plt.ylabel('Population')
    plt.title('Recovered Population Over Time')
    plt.legend()
    plt.show()
    
    plt.figure(figsize=(12, 5))
    plt.plot(t, z, label='Recovered (z)')
    plt.yscale('log')
    plt.xlabel('Time (days)')
    plt.ylabel('Log Population')
    plt.title('Recovered Population Over Time (Log Scale)')
    plt.legend()
    plt.show()
    
    plt.figure(figsize=(6, 6))
    plt.plot(y, x)
    plt.xlabel('Susceptible (y)')
    plt.ylabel('Infected (x)')
    plt.axvline(B/A, color='r', linestyle='--', label='Threshold (ρ)')
    plt.title('Phase Space Plot')
    plt.show()

# Given parameters
N = 763
x0 = 1
y0 = N - x0
z0 = 0
A = 2.18e-3  # Infection rate (day^-1)
B = 0.44  # Removal rate (day^-1)
dt = 1 / 24  # Time step (1 hour in days)
t0, t_end = 0, 25

def fx(x, y): return A * x * y - B * x

def fy(x, y): return -A * x * y

def fz(x): return B * x

t_values, x_values, y_values, z_values = euler_method(fx, fy, fz, x0, y0, z0, t0, t_end, dt)
plot_results(t_values, x_values, y_values, z_values, 'Infection Dynamics in a Boarding School')

# Find time when x reaches max
max_x_time = t_values[np.argmax(x_values)]
print(f'Maximum infected occurs at t = {max_x_time:.2f} days')

# Compute threshold values
rho = B / A
R = (A * y0) / B
print(f'Threshold value ρ = {rho:.2f}')
print(f'Reproduction number R = {R:.2f}')
if R > 1:
    print('Epidemic breaks out (R > 1).')
else:
    print('No epidemic (R ≤ 1).')
