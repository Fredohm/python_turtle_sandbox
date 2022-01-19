from turtle import Turtle, Screen
from random import randint

turtle = Turtle()
screen = Screen()
screen.screensize(1600, 900)
turtle.speed("fastest")
turtle.pensize(8)


def change_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    screen.colormode(255)
    turtle.color(red, green, blue)


def change_direction():
    direction = randint(0, 3)
    if direction % 3:
        turtle.left(90)
    elif direction % 2:
        turtle.right(90)


index = 0
while index < 1000:
    change_color()
    change_direction()
    turtle.forward(20)
    index += 1

screen.exitonclick()

