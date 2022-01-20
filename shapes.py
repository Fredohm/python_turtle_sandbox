from turtle import Turtle, Screen
from random import randint
from main import change_color

turtle = Turtle()
turtle.speed("slow")

screen = Screen()


def draw_shapes(num_sides):
    for _ in range(num_sides):
        turtle.forward(100)
        angle = 360 / sides
        turtle.right(angle)


sides = 3

while sides < 11:
    change_color(turtle, screen)
    draw_shapes(sides)
    sides += 1

screen.exitonclick()

