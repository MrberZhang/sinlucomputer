from turtle import *
from random import *


def draw_snow():
    hideturtle()
    pensize(2)
    for i in range(100):
        r, g, b = random(), random(), random()
        pencolor(r, g, b)
        penup()
        setx(randint(-350, 350))
        sety(randint(1, 270))
        pendown()
        dens = randint(8, 12)
        snow_size = randint(10, 14)
        for j in range(dens):
            forward(snow_size)
            backward(snow_size)
            right(360 / dens)


def draw_ground():
    hideturtle()
    for i in range(400):
        pensize(randint(5, 10))
        x = randint(-400, 350)
        y = randint(-280, -1)
        r, g, b = -y / 280, -y / 280, -y / 280
        pencolor((r, g, b))
        penup()
        goto(x, y)
        pendown()
        forward(randint(40, 100))


setup(800, 600, 200, 200)
tracer(False)
bgcolor('black')
draw_snow()
draw_ground()
done()
