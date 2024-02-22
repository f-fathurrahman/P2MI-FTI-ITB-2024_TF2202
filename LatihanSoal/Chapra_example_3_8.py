# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Chapra Contoh 3.8

# %% [markdown]
# Akar-akar suatu polinomial kuadrat:
# $$
# ax^2 + bx + c = 0
# $$
# diberikan oleh formula berikut
# $$
# x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
# $$
# Untuk kasus di mana $b^2 \gg 4ac$ perbedaan antara pembilang dapat menjadi sangat kecil.
# Pada kasus tersebut, kita dapat menggunakan \textit{double precision} untuk mengurangi
# kesalahan pembulatan. Selain itu, kita juga dapat menggunakan formula:
# $$
# x_{1,2} = \frac{-2c}{b \pm \sqrt{b^2 - 4ac}}
# $$
#
# Mengikuti contoh yang diberikan pada buku, kita akan menggunakan
# $a = 1$, $b = 3000.001$, dan $c = 3$. Akar-akar eksaknya adalah
# $x_{1} = -0.001$ dan $x_2 = -3000$.
#
# Buat program Python dengan menggunakan *single-precision* dan *double-precision* untuk melihat perbedaan hasil yang diberikan  dari dua formula untuk akar persamaan kuadrat.

# %% [markdown]
# Program berikut ini adalah dalam \textit{single precision}
# yang dapat Anda lengkapi. Anda juga dapat menggunakan program yang Anda tulis sendiri
# dari awal atau modifikasi dari program ini.
# ```python
# import numpy as np
#
# def calc_quad_root_v1(a, b, c):
#     D = np.float32(b**2) - np.float32(4)*a*c
#     x1 = (-b + np.sqrt(D))/(np.float32(2)*a)
#     x2 = # ... lengkapi
#     return x1, x2
#   
# def calc_quad_root_v2(a, b, c):
#     D = # ... lengkapi
#     x1 = # ... lengkapi
#     x2 = # ... lengkapi
#     return x1, x2
#   
# a = np.float32(1.0)
# b = np.float32(3000.001)
# c = np.float32(3.0)
#   
# x1_true = np.float32(-0.001)
# x2_true = np.float32(-3000.0)
#   
# x1, x2 = calc_quad_root_v1(a, b, c)
# print("Using 1st formula: approx roots: ", x1, " ", x2)
# print(type(x1), type(x2)) # pastikan x1 dan x2 merupakan np.float32
#   
# x1, x2 = calc_quad_root_v2(a, b, c)
# print(type(x1), type(x2))
# print("Using 2nd formula: approx roots: ", x1, " ", x2)  
# print("True roots: ", x1_true, " ", x2_true)
# ```
#
# Bandingkan akar-akar yang Anda peroleh dengan akar-akar eksak.
# Untuk masing-masing akar, formula mana yang memberikan hasil yang paling dekat dengan
# hasil eksak?
#
# Program berikut ini, kita akan menggunakan CAS atau \textit{computer algebra system}
# untuk memastikan bahwa formula \eqref{eq:quadeq1} dan \eqref{eq:quadeq2} memberikan
# hasil yang identik. Lengkapi kode berikut ini dan cek apakah hasil yang diberikan
# dari kedua formula tersebut adalah sama.
# ```python
# from sympy import *
#
# def calc_quad_root_v1(a, b, c):
#     D = b**2 - 4*a*c
#     x1 = (-b + sqrt(D))/(2*a)
#     x2 = (-b - sqrt(D))/(2*a)
#     return x1, x2
#   
# def calc_quad_root_v2(a, b, c):
#     D = # lengkapi ...
#     x1 = # lengkapi ...
#     x2 = # lengkapi ... 
#     return x1, x2
#   
# a = Rational(1)
# b = Rational(3000001, 1000)
# c = Rational(3)
#   
# x1_true = -Rational(1, 1000)
# x2_true = -3000
#   
# x1, x2 = calc_quad_root_v1(a, b, c)
# print("Using 1st formula: appprox roots: ", x1, " ", x2)
#
# x1, x2 = calc_quad_root_v2(a, b, c)
# print("Using 2nd formula: appprox roots: ", x1, " ", x2)
#
# print("True roots: ", x1_true, " ", x2_true)
# ```
#
# Perhatikan bahwa kode di atas juga mencetak tipe dari variabel \txtinline{x1} dan
# \txtinline{x2} adalah bilangan integer atau rasional.
# Pada SymPy, tipe untuk integer dan rasional adalah:
# ```
# <class 'sympy.core.numbers.Integer'> <class 'sympy.core.numbers.Rational'>
# ```
# Coba turunkan formula \eqref{eq:quadeq2} dari \eqref{eq:quadeq1}.

# %%
