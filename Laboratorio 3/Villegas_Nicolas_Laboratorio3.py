#Imports
from sympy import *
from sympy.abc import t

"""Pregunta 1"""

#Definición variables dependientes
x1 = Function('x1')
x2 = Function('x2')
x3 = Function('x3')

#Datos del problema
A = Matrix([[1,-1,-1],[0,2,-1],[0,0,-1]])
x = Matrix([[x1(t)],[x2(t)],[x3(t)]])

#Vector las ecuaciones 
ecuaciones = A*x

#Creación de ecuaciones
eq1 = Eq(Derivative(x1(t),t), ecuaciones[0])
eq2 = Eq(Derivative(x2(t),t), ecuaciones[1])
eq3 = Eq(Derivative(x3(t),t), ecuaciones[2])

#Creación del sistema de ecuaciones
sist = (eq1, eq2, eq3)

#Impresión de la solución del sistema
print("Solución del sistema: ", dsolve(sist))

"""Pregunta 2"""

#Definición de condiciones iniciales
t0 = 0
x0 = Matrix([[1],[1],[1]])

#Obtención de las soluciones individualmente
sol1 = dsolve(sist)[0]
sol2 = dsolve(sist)[1]
sol3 = dsolve(sist)[2]

#Creación matriz fundamental dada
fMatrix = Matrix([[exp(t), exp(2*t), 2*exp(-t)],[0, -exp(2*t), exp(-t)],[0, 0, 3*exp(-t)]])

fMatrixDet = fMatrix.subs(t, t0).det()
fMatrixDer = diff(fMatrix, t)

if(fMatrixDer == A*fMatrix and fMatrixDet != 0):
    print("Es matriz fundamental")

# La función subs fue obtenida de: https://docs.sympy.org/latest/tutorial/basic_operations.html

#Calculo de matriz inversa evaluadaa en t0
fMatrixInv = fMatrix.inv()
fMatrixInvRep = fMatrixInv.subs(t, t0)

#Calculo de la solución del PVI
result = fMatrix * fMatrixInvRep * x0

#Impresión del resultado
print("Solución del PVI: ", result)