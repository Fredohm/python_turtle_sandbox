# draw a dash line of 10 paces blank and an 10 paces drawn
# do it 15 times
from turtle import Turtle, Screen
tim = Turtle()

for _ in range(20):
    tim.forward(10)
    if _ % 2 == 0:
        tim.penup()
    else:
        tim.pendown()


screen = Screen()
screen.exitonclick()
