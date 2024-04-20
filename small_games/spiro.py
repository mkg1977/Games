import turtle
from turtle import Turtle, Screen
import random


tim = Turtle()
turtle.colormode(255)
# tim.shape("turtle")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

angle = [0, 360, 10]
tim.speed("fast")

for _ in range(36):
    tim.color(random_color())
    tim.circle(50)
    tim.left(10)