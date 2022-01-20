from turtle import Turtle, Screen
from main import change_color

turtle = Turtle()
turtle.hideturtle()
turtle.speed("fastest")

screen = Screen()

angle = 0
begin_position = turtle.position()
print(begin_position)
print(turtle.position())

while angle < 361:
    turtle = change_color(turtle, screen)
    turtle.circle(100)
    turtle.left(angle)
    angle += 1

screen.exitonclick()
