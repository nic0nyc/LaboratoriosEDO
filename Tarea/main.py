from sympy import *

x = Symbol('x')
s = Symbol('s')

a = Symbol('a')

"""

Pregunta 1

"""

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

"""

Pregunta 2

"""

#Función del solver
def solver(n, listaCoeficientes, funcion, listaCondiciones):

    try:
        func = sympify(funcion)
    except:
        print("La función no se pudo transformar")
        return

    if(n != 2 and n != 3):
        print("El solver solo funciona para n=2 y n=3")
        return

    if(len(listaCoeficientes) - 1 != n):

        print("No hay suficientes coeficientes")
        return

    if(len(listaCondiciones) != n):

        print("No hay suficientes condiciones")
        return
    
    func = laplace_transform(func, x, s, noconds=True)

    if(n == 2):


        #Resultado calculado a mano
        Ys = (func + listaCondiciones[0] * s * listaCoeficientes[2] + listaCondiciones[1] * listaCoeficientes[2] + listaCondiciones[0] * listaCoeficientes[1])/((s**2) * listaCoeficientes[2] + s * listaCoeficientes[1] + listaCoeficientes[0])

        yx = inverse_laplace_transform(Ys, s, x)

        print("Solucion Ejemplo 1 (n=2): ", yx)
    if(n == 3):

        #Resultado calculado a mano
        Ys = (func + listaCondiciones[0] * listaCoeficientes[3] * s**2 + s * listaCondiciones[1] * listaCoeficientes[3] + listaCondiciones[2] * listaCoeficientes[3] + s * listaCondiciones[0] * listaCoeficientes[2] + listaCondiciones[1] * listaCoeficientes[2] + listaCondiciones[0] * listaCoeficientes[1])/((s**3) * listaCoeficientes[3] + (s**2) * listaCoeficientes[2] + s * listaCoeficientes[1] + listaCoeficientes[0])

        yx = inverse_laplace_transform(Ys, s, x)

        print("Solucion Ejemplo 2 (n=3): ", yx)

#Probando con los ejemplos

n = 2
a2 = 1
a1 = 3
a0 = -4

fx = exp(x)

y0 = 0
y1 = 1

solver(n, [a0,a1,a2], fx, [y0,y1])

print()

n = 3
a3 = 1
a2 = -3
a1 = 3
a0 = -1

fx = 2*exp(x)

y0 = 0
y1 = 0
y2 = 0

solver(n, [a0,a1,a2,a3], fx, [y0,y1,y2])