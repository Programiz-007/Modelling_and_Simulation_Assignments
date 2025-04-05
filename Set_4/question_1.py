import numpy as np
import matplotlib.pyplot as plt


def gompertz_derivative(X):
    return -X * np.log(X)


def euler_method(f, X0, T_max, dt):
    T_values = np.arange(0, T_max, dt)
    X_values = np.zeros_like(T_values)
    X_values[0] = X0

    for i in range(1, len(T_values)):
        X_values[i] = X_values[i-1] + dt * f(X_values[i-1])
    
    return T_values, X_values


def analytical_solution(T, X0):
    return np.exp(np.exp(-T)*np.log(X0))

X_val=np.linspace(0.001,1)
X_dot=gompertz_derivative(X_val)

X_val2=np.linspace(0.1,1)
X_dot2=gompertz_derivative(X_val2)

X_val3=np.linspace(0.549,1)
X_dot3=gompertz_derivative(X_val3)

plt.plot(X_val,X_dot,label='X0=0.001')
plt.plot(X_val2,X_dot2,label='X0=0.1')
plt.plot(X_val3,X_dot3,label='X0=0.549')
plt.scatter(0.001,gompertz_derivative(0.001))
plt.scatter(0.1,gompertz_derivative(0.1))
plt.scatter(0.549,gompertz_derivative(0.549))
plt.legend()
plt.xlabel('X')
plt.ylabel('dX/dT')
plt.title('Gompertz Equation')
plt.show()


X0=0.1
T=np.arange(0,10,0.01)
T_max=10
dt=0.01

T_val,X_euler=euler_method(gompertz_derivative,X0,T_max,dt)
X_analytical=analytical_solution(T_val,X0)
plt.plot(T_val,X_euler,label='Euler',color='black')
plt.plot(T_val,X_analytical,label='Analytical',color='cyan',linestyle='--')
plt.legend()
plt.xlabel('T')
plt.ylabel('X')
plt.title("Euler and Analytical Solution")
plt.show()

relative_error = (np.abs(X_euler - X_analytical) / X_analytical)
plt.plot(T_val,relative_error,label='Rel. Error')
plt.legend()
plt.title("Relative Error")
plt.ylabel('Error')
plt.xlabel('T')
plt.show()

