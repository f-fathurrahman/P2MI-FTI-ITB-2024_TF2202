# %% [markdown]
# # This is header

# %% [markdown]
# Example again
# $$
# \alpha + \beta
# $$ 

# %%
def my_func(x):
    return x * 2


# %%
my_func(1)

# %% [markdown]
# What is the result?

# %%
my_func("a")

# %% [markdown]
# Example equation:
# $$
# \ket{1}\bra{0} 
# $$

# %% [markdown]
# # Another header

# %% [markdown]
# Cell again

# %%
import matplotlib.pyplot as plt

# %%
import matplotlib
matplotlib.style.use("dark_background")
matplotlib.rcParams.update({
    "axes.grid" : True,
    "grid.color" : "gray",
    "grid.linestyle" : "--"
})

# %%
import matplotlib_inline
matplotlib_inline.backend_inline.set_matplotlib_formats("svg")

# %%
import numpy as np

