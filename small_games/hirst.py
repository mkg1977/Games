import turtle
from turtle import Turtle, Screen
import random

color_list = [(252, 250, 245), (253, 245, 250), (238, 252, 244), (237, 243, 251),
              (244, 229, 50), (202, 7, 33), (237, 228, 2), (193, 67, 24),
              (221, 151, 81), (36, 210, 91), (240, 41, 122), (35, 92, 177),
              (32, 31, 156), (205, 11, 5), (16, 18, 53), (92, 185, 218),
              (64, 9, 44), (231, 156, 6), (58, 21, 10), (206, 31, 94),
              (219, 134, 178), (12, 201, 221), (18, 149, 28), (90, 237, 168),
              (237, 58, 31), (81, 212, 150), (96, 75, 9), (238, 160, 199),
              (87, 87, 206), (6, 37, 28), (10, 96, 62), (90, 227, 239),
              (239, 170, 161), (253, 6, 21), (254, 7, 5), (174, 178, 226),
              (3, 247, 219), (12, 57, 249), (0, 249, 253)]

turtle.colormode(255)
monty = Turtle()
monty.penup()
monty.hideturtle()
monty.speed("fast")
monty.setheading(200)
monty.forward(200)
monty.setheading(0)
no_of_step = 100

for dot_count in range(1, no_of_step + 1):
    monty.dot(20, random.choice(color_list))
    monty.forward(50)
    if dot_count % 10 == 0:
        monty.setheading(90)
        monty.forward(50)
        monty.setheading(180)
        monty.forward(500)
        monty.setheading(0)

screen = turtle.Screen()
screen.exitonclick()

