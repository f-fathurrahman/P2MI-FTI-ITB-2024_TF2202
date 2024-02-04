# %% [markdown]
# # Perhitungan simbolik

# %%

# %%

# %%

# %%

# %%
from sympy import *

# %%
g, m, c = symbols("g m c", real=True, positive=True)

# %%
v = Function("v")
t = symbols("t", real=True)

# %%
deqn = Equality( Derivative( v(t), t, 1 ), g - c/m * v(t) )
deqn

# %%
sol1 = dsolve( deqn, v(t) )
sol1

# %%
sol1.args[1].subs(t, 0)

# %%
eqn = Equality( sol1.args[1].subs(t, 0), 0 )
eqn

# %%
eqn.args[0].args[0]

# %%
C1 = eqn.args[0].args[0]
solC1 = solve(eqn, C1)
solC1

# %%
solC1[0]

# %%
solvt = sol1.subs({C1: solC1[0]})
solvt

# %%
factor(solvt.args[1])

# %% [markdown]
# # Using dsolve with ics

# %%
sol1_with_ics = dsolve( deqn, v(t), ics={ v(0) : 0 } )
sol1_with_ics

# %%
simplify( sol1_with_ics.args[1]/(g*m/c) )

# %% [markdown]
# # Nonlinear

# %%
deqn_nonlinear = Equality( Derivative( v(t), t, 1 ), g - c/m * v(t) * v(t) )
deqn_nonlinear

# %%
dsolve( deqn_nonlinear, ics={v(0): 0} )

# %%
