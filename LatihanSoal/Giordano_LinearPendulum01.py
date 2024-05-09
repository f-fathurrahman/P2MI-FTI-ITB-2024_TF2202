# %%
import numpy as np

# %%
import matplotlib.pyplot as plt
import matplotlib.style

# %%
matplotlib.style.use("dark_background")

# %%
import matplotlib_inline
matplotlib_inline.backend_inline.set_matplotlib_formats("svg")

# %% [markdown]
# # Giordano - Pendulum Linear

# %% [markdown]
# $$
# \frac{\mathrm{d}^2\theta}{\mathrm{d}t^2} = -\frac{g}{L}\theta
# $$

# %% [markdown]
# $$
# \begin{align}
# \frac{\mathrm{d}\theta}{\mathrm{d}t} & = \omega \\
# \frac{\mathrm{d}\omega}{\mathrm{d}t} & = -\frac{g}{L}\theta
# \end{align}
# $$

# %% [markdown]
# Menggunakan metode Euler:
# $$
# \begin{align}
# \theta_{i+1} & = \theta_{i} + \omega_{i}\Delta t \\
# \omega_{i+1} & = \omega_{i} - \frac{g}{L}\theta_{i} \Delta t
# \end{align}
# $$

# %% [markdown]
# Energi total:
# $$
# E = \frac{1}{2} m L^2 \omega^2 + m g L (1 - \cos(\theta))
# $$

# %% [markdown]
# Energi total untuk sudut $\theta$ yang kecil:
# $$
# E = \frac{1}{2} m L^2 \left( \omega^2 + \frac{g}{L} \theta^2 \right)
# $$

# %% [markdown]
# Untuk $\omega_{i+1}$ dan $\theta_{i+1}$ dari metode Euler:
# $$
# E_{i+1} = E_{i} + \frac{1}{2} m g L \left( \omega^{2}_{i} + \frac{g}{L} \theta^{2}_{i} \right) (\Delta t)^2
# $$

# %% [markdown]
# Dari hasil ini terlihat bahwa energi total untuk metode Euler akan semakin bertambah besar, meskipun $(\Delta t)^2$ sangat kecil.

# %%
t_final = 10.0
Δt = 0.01
int(np.ceil(t_final/Δt))

# %%
t_final = 10.0
Δt = 0.001
Nt = int(np.ceil(t_final/Δt)) + 1
print("Using Δt = ", Δt)
print("Nt       = ", Nt)
g = 9.8
L = 1.0
θ = np.zeros(Nt)
ω = np.zeros(Nt)
t = np.zeros(Nt)
θ[0] = 0.01 # initial
ω[0] = 0.0 # initial
t[0] = 0.0
m = 1.0
E = np.zeros(Nt) # Energi
E[0] = 0.5*m*L**2 * ( ω[0]**2 + g/L * θ[0]**2 )
for i in range(Nt-1):
    t[i+1] = t[i] + Δt
    ω[i+1] = ω[i] - g/L*θ[i]*Δt
    θ[i+1] = θ[i] + ω[i]*Δt
    E[i+1] = 0.5*m*L**2 * ( ω[i+1]**2 + g/L * θ[i+1]**2 )
print("Final t = ", t[-1])

# %%
plt.plot(t, θ);
plt.grid();

# %%
plt.plot(t, E);
plt.ylabel("Total energy")
plt.grid();

# %%
E[0]

# %% [markdown]
# ## Metode Euler-Cromer

# %% [markdown]
# $$
# \omega_{i+1} = \omega_{i} - \frac{g}{L} \theta_{i} \Delta t
# $$
#
# $$
# \theta_{i} = \theta_{i} + \omega_{i+1}\Delta t
# $$

# %%
t_final = 10.0
Δt = 0.001
Nt = int(np.ceil(t_final/Δt)) + 1
print("Using Δt = ", Δt)
print("Nt       = ", Nt)
g = 9.8
L = 1.0
θ = np.zeros(Nt)
ω = np.zeros(Nt)
t = np.zeros(Nt)
θ[0] = 0.01 # initial
ω[0] = 0.0 # initial
t[0] = 0.0
m = 1.0
E = np.zeros(Nt) # Energi
E[0] = 0.5*m*L**2 * ( ω[0]**2 + g/L * θ[0]**2 )
for i in range(Nt-1):
    t[i+1] = t[i] + Δt
    ω[i+1] = ω[i] - g/L*θ[i]*Δt
    θ[i+1] = θ[i] + ω[i+1]*Δt  # Euler-Cromer method
    E[i+1] = 0.5*m*L**2 * ( ω[i+1]**2 + g/L * θ[i+1]**2 )
print("Final t = ", t[-1])

# %%
plt.plot(t, θ);
plt.grid();

# %%
plt.plot(t, E);
plt.ylabel("Total energy")
plt.grid();

# %%
E[0]
