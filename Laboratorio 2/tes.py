from importlib.metadata import SelectableGroups
from re import X
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from sympy import euler

x0 = 0.0
xf = 1.0
y0 = 10**100
N = 100
h = 0.01

k = 1
c = 0.01

def f(y, x):
    return x*y

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

def solucionEDO(x):
    y = 2.72**((x**2)/2)
    return y



xp = np.arange(0.0, 1.0, 0.01)
yp = []

for n in xp:
    yp.append(solucionEDO(n))

def error(points):
    Xn,Yn = points

    E = []

    for i in range(len(Xn)):

        E.append(Yn[i])

    return (Xn, E)


plt.plot(progresivo()[0], progresivo()[1], label='progresivo', color='green')
plt.plot(xp, yp, label='solución exacta', color='orange')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.show()

plt.plot(error(progresivo())[0], error(progresivo())[1], label='Error', color='orange')
plt.legend()
plt.show()