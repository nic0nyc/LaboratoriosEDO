from sympy import *

x = Symbol('x')
s = Symbol('s')


#Función del solver
def solver(n, listaCoeficientes, funcion, listaCondiciones):

    if(n != 2 and n != 3):
        print("El solver solo funciona para n=2 y n=3")
        return

    if(len(listaCoeficientes) - 1 != n):

        print("No hay suficientes coeficientes")
        return

    if(len(listaCondiciones) != n):

        print("No hay suficientes condiciones")
        return

    func = sympify(funcion)
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

#Ejemplo 1:
n = 2
a2 = 1
a1 = 3
a0 = -4

fx = exp(x)

y0 = 0
y1 = 1

solver(n, [a0,a1,a2], fx, [y0,y1])

print()

#Ejemplo 2:

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