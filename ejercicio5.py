import math
from random import random

# Integral (lambda(2 parameters), int)
# returns: float con resultado de la doble integral de la funcion dada.
def doble_integral(funcion, repeticiones):
    result = 0
    for i in range(1,repeticiones):
        result += funcion(random(),random())/repeticiones

    return result;

# Funcion g(x,y)
g = lambda x, y: ((1/x - 1) * math.e ** -((1/x - 1) * (y + 1))) / x ** 2

# Resultados
print("Resultados de Integracion de g(x,y):")
print("10^2 Iteraciones: " + str(doble_integral(g, 100)))       # Cien
print("10^4 Iteraciones: " + str(doble_integral(g, 10000)))     # 10 Mil
print("10^6 Iteraciones: " + str(doble_integral(g, 1000000)))   # 1 Millon
