from random import random
from matplotlib import pyplot

# barslet(tuple, tuple, int)
# recive: conjunto de 4 funciones, conjunto de probababilidades donde pi es la
# probabilidad para fi, numero de iteraciones
# returns: tuple de conjunto de puntos en X y Y a plotear
def barnsley(f,p,n):
    # Puntos iniciales y grupo de puntos a plotear
    x, y = 0, 0
    points_x, points_y = [0], [0]

    # Funciones a utilizar
    f1, f2, f3, f4 = f

    for i in range(1, n):
        rand = random()

        if rand < p[0]:
            x, y = f1(x, y)

        elif rand < p[0] + p[1]:
            x, y = f2(x, y)

        elif rand < p[0] + p[1] + p[2]:
            x, y = f3(x, y)

        else:
            x, y = f4(x, y)

        points_x.append(x)
        points_y.append(y)

    return (points_x, points_y)

# Conjunto de funciones F de 4 funciones
f1 = lambda x, y: (x * 0.85 + y * 0.04, x * -0.04 + y * 0.85 + 1.6)
f2 = lambda x, y: (x * -0.15 + y * 0.28, x * 0.26 + y * 0.24 + 0.44)
f3 = lambda x, y: (x * 0.2 + y * -0.26, x * 0.23 + y * 0.22 + 1.6)
f4 = lambda x, y: (0, y * 0.16)
f = (f1,f2,f3,f4)

# Probababilidades dadas por P = {pi | P(X = i) = pi}
p = (0.85,0.07,0.07,0.01)

# Repeticiones
n = 100000

# Obtener puntos en X y Y a plotear
puntos_x, puntos_y = barnsley(f,p,n)

# Mostrar resultados con matplotlib
pyplot.scatter(puntos_x, puntos_y, s = 0.1, edgecolor ='green')
pyplot.show()
