import PIL
import random
import math
from PIL import Image, ImageDraw
from tkinter import Image, Canvas, Tk, YES, BOTH

# GLOBAL PARAMS
WIDTH = 560
HEIGHT = 560
# como tenemos las coordenadas de Tkinter en el primer pixel del canvas en 0,0 sumar un offset
OFFSET_X = WIDTH/2
OFFSET_Y = HEIGHT/2

CURRENT_X = 0
CURRENT_Y = 0
# for sherpinski
ITERATIONS = 100000

# Funciones de Sherpinski
def f1(x, y): 
    return (x/2, y/2)
def f2(x, y): 
    return (x/2 + 0.5, y/2)
def f3(x, y): 
    return (x/2 + 0.25, y/2 + 0.5)

def plot_func(iterations, prev_x, prev_y):
    for i in range(0, iterations):
        # tirar el random para seleccionar func
        rndm = random.randint(0,2)

        if rndm == 0:
            # peform the first sherpinski func
            x, y = f1(prev_x, prev_y)
            # plot the sherpinski dot
            ten_x = math.ceil(x * OFFSET_X)
            ten_y = math.ceil(y * OFFSET_Y)
            cv.create_oval(ten_x+OFFSET_X, ten_y+OFFSET_Y, ten_x+OFFSET_X, ten_y+OFFSET_Y, width = 0, fill = 'black')

        if rndm == 1:
            # peform the first sherpinski func
            x, y = f2(prev_x, prev_y)
            # plot the sherpinski dot
            ten_x = math.ceil(x * OFFSET_X)
            ten_y = math.ceil(y * OFFSET_Y)
            cv.create_oval(ten_x+OFFSET_X, ten_y+OFFSET_Y, ten_x+OFFSET_X, ten_y+OFFSET_Y, width = 0, fill = 'black')

        if rndm == 2:
            # peform the first sherpinski func
            x, y = f3(prev_x, prev_y)
            # plot the sherpinski dot
            ten_x = math.ceil(x * OFFSET_X)
            ten_y = math.ceil(y * OFFSET_Y)
            cv.create_oval(ten_x+OFFSET_X, ten_y+OFFSET_Y, ten_x+OFFSET_X, ten_y+OFFSET_Y, width = 0, fill = 'black')

        prev_x = x
        prev_y = y
    return 0

master = Tk()
master.title("Triangulo de Sherpinski")

cv = Canvas(master, width=WIDTH, height=HEIGHT, bg='white')

cv.pack(expand=YES, fill=BOTH)

# dibujar el triangulo con el numero de iteraciones actual
plot_func(ITERATIONS, CURRENT_X, CURRENT_Y)

master.mainloop()