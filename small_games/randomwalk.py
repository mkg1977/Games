from turtle import Turtle, Screen
import random
import turtle


monty = Turtle()
turtle.colormode(255)
# monty.shape("turtle")
# monty.color("red", "green")

monty.pensize(10)
monty.speed("slow")
direction = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(500):
    monty.color(random_color())
    monty.forward(25)
    monty.setheading(random.choice(direction))




screen = Screen()
screen.exitonclick()
