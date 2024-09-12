from sympy import *
init_printing()

m = symbols("m", real=True, positive=True)
g = symbols("g", real=True, positive=True)
c_d = symbols("c_d", real=True, positive=True)
t = symbols("t", real=True, positive=True)

# Analytic solution
analytic_sol = sqrt(g*m/c_d) * tanh(sqrt(g*c_d/m)*t)
v = analytic_sol

RHS = diff(v, t)
LHS = g - c_d/m * v**2

num_values = {
    m: 68.1,
    t: 12.0,
    c_d: 0.25,
    g: 9.8
}

RHS.subs(num_values)
LHS.subs(num_values)
