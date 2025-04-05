import numpy as np
import matplotlib.pyplot as plt

def richardson_euler(x0, y0, k, l, g, h, alpha, beta, dt, T):
    n_steps = int(T / dt)
    t_values = np.linspace(0, T, n_steps)
    x_values = np.zeros(n_steps)
    y_values = np.zeros(n_steps)
    
    x_values[0] = x0
    y_values[0] = y0
    
    for i in range(1, n_steps):
        x_dot = k * y_values[i - 1] + g - alpha * x_values[i - 1]
        y_dot = l * x_values[i - 1] + h - beta * y_values[i - 1]
        
        x_values[i] = x_values[i - 1] + dt * x_dot
        y_values[i] = y_values[i - 1] + dt * y_dot
    
    return t_values, x_values, y_values

def plot_results(t_values, x_values, y_values, title):
    plt.figure(figsize=(10, 5))
    plt.plot(t_values, x_values, label='x (Nation 1)')
    plt.plot(t_values, y_values, label='y (Nation 2)')
    plt.yscale('log')
    plt.xlabel('Time')
    plt.ylabel('War-waging potential')
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()
    
    plt.figure(figsize=(5, 5))
    plt.plot(x_values, y_values)
    plt.xlabel('x (Nation 1)')
    plt.ylabel('y (Nation 2)')
    plt.title(f'Phase plot: {title}')
    plt.grid()
    # plt.ylim(0,8)
    plt.show()

# Scenario A: Mutual disarmament without grievance
# params_A = dict(x0=7, y0=8, k=0.8, l=2, g=0, h=0, alpha=3, beta=5, dt=0.002, T=5)
# t_A, x_A, y_A = richardson_euler(**params_A)
# plot_results(t_A, x_A, y_A, 'Mutual Disarmament Without Grievance')

# Scenario B: Mutual disarmament with grievance
# params_B = dict(x0=0, y0=0, k=3, l=0.85, g=6, h=5.5, alpha=4, beta=5, dt=0.001, T=5)
# t_B, x_B, y_B = richardson_euler(**params_B)
# plot_results(t_B, x_B, y_B, 'Mutual Disarmament With Grievance')

# # Scenario C: Unilateral disarmament
# params_C = dict(x0=250, y0=0, k=2, l=2, g=4, h=5, alpha=3, beta=7, dt=0.002, T=5)
# t_C, x_C, y_C = richardson_euler(**params_C)
# plot_results(t_C, x_C, y_C, 'Unilateral Disarmament')

# # Scenario D: Arms race
params_D = dict(x0=250, y0=500, k=2, l=1, g=0, h=0, alpha=0, beta=0, dt=0.001, T=10)
t_D, x_D, y_D = richardson_euler(**params_D)
plot_results(t_D, x_D, y_D, 'Arms Race')