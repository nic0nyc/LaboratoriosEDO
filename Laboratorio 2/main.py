from importlib.metadata import SelectableGroups
from re import X
import numpy as np
import matplotlib.pyplot as plt

x0 = 0.0
xf = 1.0
y0 = 10**100
N = 100
h = 0.01

k = 1
c = 0.01

def f(x, y, k, c):
    return k*y**(1+c)

def progresivo():
    X = np.zeros(N + 1)
    Y = np.zeros(N + 1)

    X[0] = x0
    Y[0] = y0

    for n in range(N):
        
        if n==0:
            y = y0 + h*f(x0, y0, k, c)
            x = x0 + h*n
            X[n+1] = x
            Y[n+1] = y

        else:
            y = y + h*f(x, y, k, c)
            x = x + h*n
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
            yT = y0 + (h/2)*f(x0, y0, k, c)
            y = y0 + h* f(xT, yT, k, c)
            x = x0 + h*n
            X[n+1] = x
            Y[n+1] = y

        else:
            xT = x + h/2
            yT = y + (h/2)*f(x, y, k, c)
            y = y + h * f(xT, yT, k, c)
            x = x + h*n
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
            yT = y0 + h*f(x0, y0, k, c)
            x = x0 + h*n
            y = y0 + (h/2) * (f(x0, y0, k, c) + f(x0, yT, k, c))
            X[n+1] = x
            Y[n+1] = y
        else:
            yT = y + h*f(x, y, k, c)
            x = x + h*n
            y = y + (h/2) * (f(x, y, k, c) + f(x, yT, k, c))
            X[n+1] = x
            Y[n+1] = y
    return (X, Y)

def solucionExacta(x):
    return (1/((y0**(-c)) - c*k*x))**(1/c)

        

"""
plt.plot(x,y1,label='k=-1.0',color='red')
plt.plot(x,y2,label='k=0.3',color='green')
plt.plot(x,y3,label='k=1.0',color='blue')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.show()
"""

xp = np.arange(0.0, 1.0, 0.01)

plt.plot(xp, solucionExacta(xp), label='solución exacta', color='pink')
plt.plot(modificado()[0], modificado()[1], label='modificado', color='red')
plt.plot(heun()[0], heun()[1], label='heun', color='green')
plt.plot(progresivo()[0], progresivo()[1], label='progresivo', color='blue')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.show()