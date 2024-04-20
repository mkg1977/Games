from turtle import Turtle, Screen
import random
import turtle


monty = Turtle()
turtle.colormode(255)
# monty.shape("turtle")
# monty.color("red", "green")

monty.speed("fast")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(72):
    monty.color(random_color())
    monty.circle(100)
    monty.left(5)





screen = Screen()
screen.exitonclick()