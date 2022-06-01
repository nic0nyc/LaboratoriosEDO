from sympy import *

x = Symbol('x')
s = Symbol('s')

def TLaplace(func):
    return integrate(exp(-s*x) * func, (x, 0, oo), conds='none')

functionsList = [sin((5*x)/2), cos((5*x)/2), x**13, (x**2)*sin(2*x), exp(-3*x), exp(3*x)*sin(2*x)]

for func in functionsList:
    
    print(f"Mio: {TLaplace(func)}")
    print(f"Funcion: {laplace_transform(func, x , s, noconds=True)}")

    print()