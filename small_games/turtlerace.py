from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=1000, height=800)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color from rainbow: ")
turtle_colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_positions = [-300, -200, -100, 0, 100, 200, 300]
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-450, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 480:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You've won! The {wining_color} turtle is the winner!")
            else:
                print(f"You've lost. The {wining_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()