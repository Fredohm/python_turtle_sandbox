from turtle import Turtle, Screen
from main import change_color
turtle = Turtle()
screen = Screen()

for _ in range(20):
    turtle.forward(10)
    if _ % 2 == 0:
        turtle.penup()
    else:
        turtle = change_color(turtle, screen)
        turtle.pendown()

screen.exitonclick()
