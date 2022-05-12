from sympy import *
from sympy.abc import t
from sympy.abc import tau

#   Pregunta 1

x1 = Function('x1')
x2 = Function('x2')
x3 = Function('x3')

eq1 = Eq(Derivative(x1(t),t), x1(t) - x2(t) - x3(t))
eq2 = Eq(Derivative(x2(t),t), 2*x2(t) - x3(t))
eq3 = Eq(Derivative(x3(t),t), -x3(t))

sist = (eq1, eq2, eq3)

print("Solución del sistema: ", dsolve(sist))

#   Pregunta 2

sol1 = dsolve(sist)[0]
sol2 = dsolve(sist)[1]
sol3 = dsolve(sist)[2]

fMatrix = Matrix([[exp(t), exp(2*t), 2*exp(-t)],[0, -exp(2*t), exp(-t)],[0, 0, 3*exp(-t)]])

f1 = fMatrix[0,0] + fMatrix[0,1] + fMatrix[0,2]
f2 = fMatrix[1,0] + fMatrix[1,1] + fMatrix[1,2]
f3 = fMatrix[2,0] + fMatrix[2,1] + fMatrix[2,2]

constantes = [("C1", 3),("C2", 1),("C3", -1)]

# La función args fue obtenida de: https://stackoverflow.com/questions/38418205/get-a-value-from-solution-set-returned-as-finiteset-by-sympy
# La función subs fue obtenida de: https://docs.sympy.org/latest/tutorial/basic_operations.html

sol1Changed = sol1.args[1].subs(constantes)
sol2Changed = sol2.args[1].subs(constantes)
sol3Changed = sol3.args[1].subs(constantes)

# Como cumple (x' = A*c) para el vector de solución homogenea "x" obtenido antes (con constantes C1 = 3, C2 = 1 y C3 = -1) y un vector de constantes (c = (1 ,1,1)), por lo tanto, es matriz fundamental.
if(f1 == sol1Changed and f2 == sol2Changed and f3 == sol3Changed):
    print("Es matriz fundamental")

t0 = 0
x0 = Matrix([1,1,1])

fMatrixInv = fMatrix.inv()
fMatrixInvRep = fMatrixInv.subs(t, t0)

result = fMatrix * fMatrixInvRep * x0

print("Solución del PVI: ", result)