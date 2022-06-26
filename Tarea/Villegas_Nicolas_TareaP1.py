from sympy import *

x = Symbol('x')
s = Symbol('s')

a = Symbol('a')


#Mi método a través de la definición
def TLaplace(func):
    return integrate(exp(-s*x) * func, (x, 0, oo), conds='none')

#Lista de las funciones
functionsList = [sin((5*x)/2), cos((5*x)/3), x**13, (x**2)*sin(2*x), exp(-3*x), exp(3*x)*sin(2*x)]

#Comparación e impresión de los resultados
for func in functionsList:
    
    print(f"La función es: {func}")
    print(f"Solución a través de mi método: {TLaplace(func)}")
    print(f"Solución con el método de python: {laplace_transform(func, x , s, noconds=True)}")
    
    # https://docs.sympy.org/dev/tutorial/gotchas.html#equals-signs
    if((simplify(TLaplace(func) - laplace_transform(func, x , s, noconds=True))) == 0):
        print("Las transformadas son iguales")

    print()