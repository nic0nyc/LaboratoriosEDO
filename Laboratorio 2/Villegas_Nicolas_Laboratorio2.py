from importlib.metadata import SelectableGroups
from re import X
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

x0 = 0.0
xf = 1.0
y0 = 10**100
N = 100
h = 0.01

k = 1
c = 0.01

def f(y, x):
    return k*y**(1+c)

def progresivo():
    X = np.zeros(N + 1)
    Y = np.zeros(N + 1)

    X[0] = x0
    Y[0] = y0

    for n in range(N):
        
        if n==0:
            y = y0 + h*f(y0, x0)
            x = x0 + h
            X[n+1] = x
            Y[n+1] = y

        else:
            y = y + h*f(y, x)
            x = x + h
            X[n+1] = x
            Y[n+1] = y
    return (X, Y)

def modificado():
    X = np.zeros(N + 1)
    Y = np.zeros(N + 1)

    X[0] = x0
    Y[0] = y0

    for n in range(N):
        
        if n==0:
            xT = x0 + h/2
            yT = y0 + (h/2)*f(y0, x0)
            y = y0 + h* f(yT, xT)
            x = x0 + h
            X[n+1] = x
            Y[n+1] = y

        else:
            xT = x + h/2
            yT = y + (h/2)*f(y, x)
            y = y + h * f(yT, xT)
            x = x + h
            X[n+1] = x
            Y[n+1] = y
    return (X, Y)


def heun():
    X = np.zeros(N + 1)
    Y = np.zeros(N + 1)

    X[0] = x0
    Y[0] = y0

    for n in range(N):
        
        if n==0:
            yT = y0 + h*f(x0, y0)
            x = x0 + h
            y = y0 + (h/2) * (f(y0, x0) + f(yT, x0))
            X[n+1] = x
            Y[n+1] = y
        else:
            yT = y + h*f(x, y)
            x = x + h
            y = y + (h/2) * (f(y, x) + f(yT, x))
            X[n+1] = x
            Y[n+1] = y
    return (X, Y)        

def solucionEDO(x):
    y = (1/(y0**(-c) - c*k*x))**(1/c)
    return y



xp = np.arange(0.0, 1.0, 0.01)
yp = []

for n in xp:
    yp.append(solucionEDO(n))

def error(points):
    Xn,Yn = points
    E = []

    for i in range(len(Xn)):
        E.append(abs(Yn[i] - solucionEDO(Xn[i])))
    
    return (Xn, E)



plt.plot(xp, yp, label='Solución exacta', color='orange')
plt.plot(modificado()[0], modificado()[1], label='Euler modificado', color='red')
plt.plot(heun()[0], heun()[1], label='Heun', color='green')
plt.plot(progresivo()[0], progresivo()[1], label='Euler progresivo', color='blue')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.show()

plt.plot(error(progresivo())[0], error(progresivo())[1], label='Error Progresivo', color='orange')
plt.plot(error(modificado())[0], error(modificado())[1], label='Error Modificado', color='green')
plt.plot(error(heun())[0], error(heun())[1], label='Error Heun', color='blue')
plt.legend()
plt.show()

"""
Pregunta 1:  El euler modificado fue el que mejor aproximó, esto porque su error fue el menor.
Pregunta 2: Esto se debe a que el T no es parte del dominio de la función, entonces es para poder expresar esto en python.
"""