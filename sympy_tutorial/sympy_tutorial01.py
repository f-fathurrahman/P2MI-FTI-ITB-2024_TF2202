# %% [markdown]
# SymPy adalah pustaka Python untuk melakukan perhitungan matematika simbolik. Dalam hal ini, SymPy dapat digolongkan
# sebagai CAS (*computer algebra system*). Fitur-fitur dari SymPy masih terbatas jika dibandingkan dengan aplikasi
# CAS lain yang mapan, seperti Wolfram (dulunya bernama Mathematica), Maple, dsb. Meskipun demikian SymPy sudah dapat digunakan untuk memudahkan manipulasi simbolik dari persamaan matematik yang sering ditemui pada sains dan teknik. 

# %%
from sympy import *

# %%
x = symbols("x")

# %%
x + x

# %%
x * x + 3*x

# %%
(x * x + 3*x)/x**4

# %%
simplify((x * x + 3*x)/x**4)

# %%
apart((x * x + 3*x)/x**4)

# %% [markdown]
# Konstanta

# %%
sin(2*pi)

# %%
E**(2*pi)

# %%
E**(I*pi)

# %%
E**2 + E**2

# %%
Paksa menjadi bentuk numerik

# %%
expr1 = E**2 + E**2
expr1.evalf()

# %%
expr1 = sin(2*pi/3)
expr1

# %%
expr1.evalf()

# %%
N(expr1)

# %% [markdown]
# Hati-hati menggunakan `N` sebagai nama variabel.

# %%
s = Integer(1) / Integer(3)
s

# %%
s = 1/3
s

# %%
