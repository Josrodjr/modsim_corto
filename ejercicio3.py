from time import time
from random import random

# class generators
# contine generadores de numeros pseudo-random
class generators:

    def __init__(self):
        self.gen1 = int(time() * 1000)      # seed generator1
        self.gen2 = int(time() * 1000)      # seed generator2

    # generator1
    # return: float aleatorio entre [0,1)
    def generator1(self):
        self.gen1 = (5 ** 5 * self.gen1) % (2 ** 35 - 1)
        return self.gen1/(2 ** 35 - 1)

    # generator2
    # return: float aleatorio entre [0,1)
    def generator2(self):
        self.gen2 = (7 ** 5 * self.gen2) % (2 ** 31 - 1)
        return self.gen2/(2 ** 31 - 1)

# permite al usuario ingresar el numero de repeticiones a realizar
repeticiones = 0
while(repeticiones == 0):
    try:
        repeticiones = int(input("Ingrese numero de repeticiones: "))
    except ValueError:
        print("Ingrese unicamente numeros")

# pseudo-random-generator y tuple de generadores a correr
gens = generators()
ramdom_gens = (gens.generator1, gens.generator2, random)

for gen in ramdom_gens:
    # diccionario para guardar resultados
    numbers = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}

    # se corre el generador la cantidad de repreticiones
    for i in range(repeticiones):
        numbers[str(int(gen() * 10))] += 1

    # se imprime nombre del metodo y los resultados con un histograma
    print(gen.__name__)
    for key, val in numbers.items():
        print("0." + key + "-" + str((int(key) + 1)/10)+ " => " + \
        "*" * int(500 * (val/repeticiones)) + " (" + str(val) + ","\
        + str(round(val/repeticiones * 100, 3)) + "%)")
