import numpy as np
import matplotlib.pyplot as plt

def lanchester_euler(J0, A0, a, j, dt=1):
    J, A = [J0], [A0]
    t = [0]
    
    while J[-1] > 1 and A[-1] > 1:
        J_new = J[-1] - a * A[-1] * dt
        A_new = A[-1] - j * J[-1] * dt
        J.append(max(J_new,0))  # Ensure non-negative values
        A.append(max(A_new,0))
        t.append(t[-1] + dt)
    
    return np.array(t), np.array(J), np.array(A)

# Given parameters
J_= 18274
A_=66454
a=0.0106
j=0.0544
t, J, A = lanchester_euler(J_, A_, a, j)

print("Japan",J)
print(J.size)

# Lanchester's Square Law Prediction
pred_outcome = A_**2 - J_**2 * (j/a)
print("Predicted Outcome: American Victory" if pred_outcome > 0 else "Japanese Victory")

# Final results
print(f"Battle lasted {t[-1]} days")
print(f"Final Troops - Americans: {A[-1]:.0f}, Japanese: {J[-1]:.0f}")
print(f"Casualties - Americans: {A_ - A[-1]:.0f}, Japanese: {J_ - J[-1]:.0f}")

# Plot J(t) and A(t)
plt.figure(figsize=(10,5))
plt.plot(t, J, label='Japanese Troops')
plt.plot(t, A, label='American Troops')
plt.xlabel('Time (days)')
plt.ylabel('Number of Troops')
plt.legend()
plt.title('Troop Strength Over Time')
plt.grid()
plt.show()

# Log plot
plt.figure(figsize=(10,5))
plt.semilogy(t, J, label='Japanese Troops')
plt.semilogy(t, A, label='American Troops')
plt.xlabel('Time (days)')
plt.ylabel('Number of Troops (log scale)')
plt.legend()
plt.title('Log-Scale Troop Strength Over Time')
plt.grid()
plt.show()

# Plot A vs. J
plt.figure(figsize=(6,6))
plt.plot(J, A, label='A vs J')
plt.xlabel('Japanese Troops')
plt.ylabel('American Troops')
plt.title('American Troops vs Japanese Troops')
plt.grid()
plt.legend()
plt.show()
