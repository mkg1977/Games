from turtle import Turtle, Screen
import random

monty = Turtle()
monty.shape("turtle")
monty.color("red", "green")

colors = ["red", "blue", "green", "orange", "violet", "purple", "magenta", "cyan", "maroon", "navy"]

def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        monty.forward(100)
        monty.right(angle)

for shape_sides in range(3, 11):
    monty.color(random.choice(colors))
    draw_shapes(shape_sides)




screen = Screen()
screen.exitonclick()