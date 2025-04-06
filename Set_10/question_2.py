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
        z_values[i] = z_values[i-1] + dt * fz(x_values[i-1],z_values[i-1])
    
    return t_values, x_values, y_values, z_values

def plot_results(t, x, y, z):
    plt.figure(figsize=(12, 5))
    plt.plot(t, x, label='Infected (x)')
    plt.xlabel('Time (years)')
    plt.ylabel('Population')
    plt.title('Infected Population Over Time')
    plt.legend()
    plt.show()
    
    plt.figure(figsize=(12, 5))
    plt.plot(t, y, label='Susceptible (y)')
    plt.xlabel('Time (years)')
    plt.ylabel('Population')
    plt.title('Susceptible Population Over Time')
    plt.legend()
    plt.show()
    
    plt.figure(figsize=(12, 5))
    plt.plot(t, z, label='Recovered (z)')
    plt.xlabel('Time (years)')
    plt.ylabel('Population')
    plt.title('Recovered Population Over Time')
    plt.legend()
    plt.show()

# Given parameters
N = 1_000_000
x0 = 100_000
y0 = 900_000
z0 = 0
A = 1e-6  # Infection rate (year^-1)
B = 0.333  # Removal rate (year^-1) 
a = 0.02  # Death rate (year^-1)
b = 0.02  # Birth rate (year^-1)
dt = 1 / 365  # Time step (1 day in years)
t0, t_end = 0, 150

def fx(x, y): return A * x * y - B * x - a * x

def fy(x, y): return b * N - A * x * y - a * y

def fz(x,z): return B * x - a * z

t_values, x_values, y_values, z_values = euler_method(fx, fy, fz, x0, y0, z0, t0, t_end, dt)
plot_results(t_values, x_values, y_values, z_values)

# Find times when x reaches peaks
from scipy.signal import find_peaks
peaks, _ = find_peaks(x_values)
peak_times = t_values[peaks]
print(f'Endemic breakouts occur at times: {peak_times}')
