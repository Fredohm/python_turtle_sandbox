from random import randint


def change_color(turtle, screen):
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    screen.colormode(255)
    turtle.color(red, green, blue)
    return turtle

