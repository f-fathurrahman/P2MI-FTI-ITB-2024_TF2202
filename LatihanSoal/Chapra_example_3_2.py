# %% [markdown]
# # Chapra Contoh 3.2

# %% [markdown]
# Scarborough memberikan suatu kriteria yang menghubungkan antara jumlah digit signifikan
# dengan dan nilai aproksimasi. Menurut kriteria ini, jika menggunakan:
# \begin{equation}
# \epsilon_{s} = (0.5 \times 10^{2-n})\%
# \end{equation}
# maka hasil yang diperoleh akan benar untuk setidaknya $n$ digit signifikan.

# %% [markdown]
# Fungsi eksponensial dapat dihitung dengan menggunakan deret sebagai berikut:
# $$
# e^{x} = 1 + x + \frac{x^2}{2} + \frac{x^3}{3!} + \cdots + \frac{x^n}{n!}
# $$
# Kita ingin menggunakan Persamaan ini untuk menghitung estimasi
# dari $e^{0.5}$ untuk setidaknya tiga digit signifikan.
# Dengan menggunakan kriteria dari Scarborough, nilai $n=3$ diperoleh:
# $$
# \epsilon_{s} = (0.5 \times 10^{2-3}) \% = 0.05 \%
# $$
# Kita akan menambahkan suku-suku pada deret Taylor sampai $\epsilon_{a}$ lebih kecil dari $\epsilon_{s}$.

# %% [markdown]
# Ulangi perhitungan ini untuk jumlah digit signifikan yang berbeda, misalnya 5, 8, dan 10
# digit signifikan. Silakan melakukan modifikasi terhadap program yang diberikan.
