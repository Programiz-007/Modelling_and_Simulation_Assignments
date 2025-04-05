import numpy as np
import matplotlib.pyplot as plt

# Euler integration of Lanchester model
def euler_lanchester(F0, B0, f, b, dt, stop_condition):
    F = [F0]
    B = [B0]
    t = [0]
    while not stop_condition(F[-1], B[-1]):
        F_new = F[-1] - b * B[-1] * dt
        B_new = B[-1] - f * F[-1] * dt
        t_new = t[-1] + dt
        F.append(F_new)
        B.append(B_new)
        t.append(t_new)
    return np.array(t), np.array(F), np.array(B)

# Stage A
f = b = 0.05
dt = 1
F0_A, B0_A = 3, 13
cond_A = lambda F, B: F <= 2 and F > 1
t_A, F_A, B_A = euler_lanchester(F0_A, B0_A, f, b, dt, cond_A)
final_B_A = B_A[-1]

# Stage B
F0_B = F_A[-1] + 17
B0_B = final_B_A + 14
cond_B = lambda F, B: F <= 2 and F > 1
t_B, F_B, B_B = euler_lanchester(F0_B, B0_B, f, b, dt, cond_B)
t_B += t_A[-1]
final_B_B = B_B[-1]

# Stage C
F0_C = F_B[-1] + 13
B0_C = final_B_B
cond_C = lambda F, B: F < 1
t_C, F_C, B_C = euler_lanchester(F0_C, B0_C, f, b, dt, cond_C)
t_C += t_B[-1]

# Full battle scenario (Part D)
f_d = b_d = 0.1
F0_D, B0_D = 33, 27
cond_D = lambda F, B: F <= 0 or B <= 0
t_D, F_D, B_D = euler_lanchester(F0_D, B0_D, f_d, b_d, dt, cond_D)

# Plotting
plt.figure(figsize=(12, 7))
# Three-stage battle
plt.plot(t_A, F_A, label="French (Stage A)", linestyle='-')
plt.plot(t_A, B_A, label="British (Stage A)", linestyle='--')
plt.plot(t_B, F_B, label="French (Stage B)", linestyle='-')
plt.plot(t_B, B_B, label="British (Stage B)", linestyle='--')
plt.plot(t_C, F_C, label="French (Stage C)", linestyle='-')
plt.plot(t_C, B_C, label="British (Stage C)", linestyle='--')
# Full engagement battle
plt.plot(t_D, F_D, label="French (Full Battle)", linestyle='-.')
plt.plot(t_D, B_D, label="British (Full Battle)", linestyle=':')
plt.xlabel("Time")
plt.ylabel("Number of Ships")
plt.title("Battle of Trafalgar: Multi-Stage vs Full Fleet Engagement")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
