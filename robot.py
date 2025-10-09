import sympy as sp
sp.init_printing(use_unicode=True)
a, b, c = sp.symbols('a b c')

A = sp.Matrix([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
A.det()
A.T
A.inv()
A * b