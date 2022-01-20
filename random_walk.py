from turtle import Turtle, Screen
from random import randint
from main import change_color


turtle = Turtle()
turtle.hideturtle()
screen = Screen()
screen.screensize(1600, 900)
turtle.speed("fastest")
turtle.pensize(8)


def change_direction():
    direction = randint(0, 3)
    if direction % 3:
        turtle.left(90)
    elif direction % 2:
        turtle.right(90)


index = 0
while index < 1000:
    turtle = change_color(turtle, screen)
    change_direction()
    turtle.forward(20)
    index += 1

screen.exitonclick()

