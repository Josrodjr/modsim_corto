import math
import random

# Integral (lambda(2 parameters), int)
# returns: float con resultado de la doble integral de legal
# funcion dada.
def doble_integral(funcion, repeticiones):
    result = 0
    for i in range(1,repeticiones):
        result += funcion(random.random(),random.random())/i

    return result;

# Funcion g(x,y)
g = lambda x, y: (math.e ** -(x ** 2 + 1/y - 1)) * (x / y ** 2)

# Resultados
print("Resultados de Integracion de g(x,y):")
print("10^2 Iteraciones: " + str(doble_integral(g, 100)))       # Cien
print("10^4 Iteraciones: " + str(doble_integral(g, 10000)))     # 10 Mil
print("10^6 Iteraciones: " + str(doble_integral(g, 1000000)))   # 1 Millon
