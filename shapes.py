from turtle import Turtle, Screen
from random import randint

turtle = Turtle()
turtle.speed("slow")

screen = Screen()


def draw_shapes(num_sides):
    for _ in range(num_sides):
        turtle.forward(100)
        angle = 360 / sides
        turtle.right(angle)


def change_color():
    r = randint(0, 256)
    g = randint(0, 256)
    b = randint(0, 256)
    screen.colormode(255)
    turtle.color(r, g, b)


sides = 3

while sides < 11:
    change_color()
    draw_shapes(sides)
    sides += 1

screen.exitonclick()

