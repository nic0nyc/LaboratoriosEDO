#Imports
from sympy import *
from sympy.abc import t

"""Pregunta 1"""

#Definición variables dependientes
x1 = Function('x1')
x2 = Function('x2')
x3 = Function('x3')

#Creación de ecuaciones
eq1 = Eq(Derivative(x1(t),t), x1(t) - x2(t) - x3(t))
eq2 = Eq(Derivative(x2(t),t), 2*x2(t) - x3(t))
eq3 = Eq(Derivative(x3(t),t), -x3(t))

#Creación del sistema de ecuaciones
sist = (eq1, eq2, eq3)

#Impresión de la solución del sistema
print("Solución del sistema: ", dsolve(sist))

"""Pregunta 2"""

#Obtención de las soluciones individualmente
sol1 = dsolve(sist)[0]
sol2 = dsolve(sist)[1]
sol3 = dsolve(sist)[2]

#Creación matriz fundamental dada
fMatrix = Matrix([[exp(t), exp(2*t), 2*exp(-t)],[0, -exp(2*t), exp(-t)],[0, 0, 3*exp(-t)]])

#Transformación de la matriz recomendada a sus filas individuales
f1 = fMatrix[0,0] + fMatrix[0,1] + fMatrix[0,2]
f2 = fMatrix[1,0] + fMatrix[1,1] + fMatrix[1,2]
f3 = fMatrix[2,0] + fMatrix[2,1] + fMatrix[2,2]

#Constantes para poder igualar a la matriz fundamental por el vector (1,1,1), obtenidas a travez de calculos matematicos.
constantes = [("C1", 3),("C2", 1),("C3", -1)]

# La función args fue obtenida de: https://stackoverflow.com/questions/38418205/get-a-value-from-solution-set-returned-as-finiteset-by-sympy
# La función subs fue obtenida de: https://docs.sympy.org/latest/tutorial/basic_operations.html

#Soluciones individuales con las constantes reemplazadas.
sol1Changed = sol1.args[1].subs(constantes)
sol2Changed = sol2.args[1].subs(constantes)
sol3Changed = sol3.args[1].subs(constantes)

# Como cumple (x' = A*c) para el vector de solución homogenea "x" obtenido antes (con constantes C1 = 3, C2 = 1 y C3 = -1) y un vector de constantes (c = (1 ,1,1)), por lo tanto, es matriz fundamental.
if(f1 == sol1Changed and f2 == sol2Changed and f3 == sol3Changed):
    print("Es matriz fundamental")

#Definición de condiciones iniciales
t0 = 0
x0 = Matrix([1,1,1])

#Calculo de matriz inversa evaluadaa en t0
fMatrixInv = fMatrix.inv()
fMatrixInvRep = fMatrixInv.subs(t, t0)

#Calculo de la solución del PVI
result = fMatrix * fMatrixInvRep * x0

#Impresión del resultado
print("Solución del PVI: ", result)