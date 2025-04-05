import numpy as np
import matplotlib.pyplot as plt


def dX_dt(X, A):
    return (X + A) * (1 - X)


def X_T(T, A, X0):
    return ((X0 + A) * np.exp(T) - A) / (1 + (X0 + A) * np.exp(T))


A_values = [0, 0.2, 0.5]


plt.figure(figsize=(8, 5))
for A in A_values:
    X_vals = np.linspace(-A, 1, 400)
    dX_vals = dX_dt(X_vals, A)
    plt.plot(X_vals, dX_vals, label=f"A = {A}")

plt.xlabel("X")
plt.ylabel("dX/dT")
plt.title("Phase Plot of the Agricultural Innovation Spread Model")
plt.axhline(0, color='k', linestyle='--', linewidth=0.8)
plt.axvline(0, color='k', linestyle='--', linewidth=0.8)
plt.legend()
plt.show()


T_vals = np.linspace(0, 30, 500)
X0 = 0.0001 

plt.figure(figsize=(8, 5))
for A in A_values:
    X_vals = X_T(T_vals, A, X0)
    plt.plot(T_vals, X_vals, label=f"A = {A}")

plt.xlabel("T")
plt.ylabel("X(T)")
plt.title("Solution of the Spread of Innovation Model")
plt.legend()
plt.grid(True)
plt.show()
