from turtle import Turtle, Screen
from main import change_color

turtle = Turtle()
turtle.hideturtle()
turtle.speed("fastest")

screen = Screen()

begin_position = turtle.position()
print(begin_position)
print(turtle.position())

size_of_gap = 3
for _ in range(int(360 / size_of_gap)):
    turtle = change_color(turtle, screen)
    turtle.circle(100)
    turtle.setheading(turtle.heading() + size_of_gap)

screen.exitonclick()
