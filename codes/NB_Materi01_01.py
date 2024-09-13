# %% [markdown]
# # Review Jupyter Notebook

# %% [markdown]
# This is a *text*.
#
# This is a **text**.
#
# This is a text.
#
# This is a text.

# %% [markdown]
# ## Subheader

# %% [markdown]
# Teks lagi. Teks lagi.

# %% [markdown]
# # This is header

# %% [markdown]
# Ini contoh persamaan display (*display equation*), terpisah dari paragraf:
# $$
# \alpha + \beta
# $$

# %% [markdown]
# Inline equation: contoh alfabet Yunani: $\alpha$, $\beta$, $\gamma$, 

# %% [markdown]
# $$
# \int_{-\infty}^{\infty} \exp \left( -\frac{1}{2}x^2 \right) \, \mathrm{d}x
# $$

# %% [markdown]
# $$
# \begin{align}
# E_0 & = mc^2 \\
# E   & = 
# \frac{mc^2}{\sqrt{1-\frac{v^2}{c^2}}}
# \end{align}
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


# %% [markdown]
# https://discuss.boardinfinity.com/t/advantages-and-disadvantages-of-jupyter-lab/5561

# %% [markdown]
# Advantages of Jupyter Notebook
#
# There are the following advantages of Jupyter Notebook -
#
#     All in one place: As you know, Jupyter Notebook is an open-source web-based interactive environment that combines code, text, images, videos, mathematical equations, plots, maps, graphical user interface and widgets to a single document.
#     Easy to convert: Jupyter Notebook allows users to convert the notebooks into other formats such as HTML and PDF. It also uses online tools and nbviewer which allows you to render a publicly available notebook in the browser directly.
#     Easy to share: Jupyter Notebooks are saved in the structured text files (JSON format), which makes them easily shareable.
#     Language independent: Jupyter Notebook is platform-independent because it is represented as JSON (JavaScript Object Notation) format, which is a language-independent, text-based file format. Another reason is that the notebook can be processed by any programing language, and can be converted to any file formats such as Markdown, HTML, PDF, and others.
#     Interactive code: Jupyter notebook uses ipywidgets packages, which provide many common user interfaces for exploring code and data interactivity.
#
# Disadvantages of Jupyter Notebook
#
# There are the following disadvantages of Jupyter Notebook:
#
#     It is very hard to test long asynchronous tasks.
#     Less Security
#     It runs cell out of order
#     In Jupyter notebook, there is no IDE integration, no linting, and no code-style correction.
#

# %%
x = 1.0

# %%
a = 2 + x
a

# %%
x = 3.3

# %%
