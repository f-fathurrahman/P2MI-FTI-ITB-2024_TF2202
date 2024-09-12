import numpy as np
import matplotlib.pyplot as plt

def calc_analytic_sol(m, g, c, t):
    v = g*m/c * (1 - np.exp(-c/m*t))
    return v

m = 68.1
g = 9.81
c = 12.5

t = 10.0
print("t = 10.0, v = ", calc_analytic_sol(m, g, c, t), " m/s")

t = np.linspace(0.0, 15.0, 200)
plt.plot(t, calc_analytic_sol(m, g, c, t))
plt.grid(True)
plt.show()
