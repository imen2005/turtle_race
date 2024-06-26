from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []



for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])

if user_bet:
    is_race_on = True

while is_race_on:
    for turt in all_turtles:
        if turt.xcor() > 230:
            is_race_on = False
            winning_color = turt.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lost! The {winning_color} turtle is the winner.")
        else:
            random_distance = random.randint(0,10)
            turt.forward(random_distance)
screen.exitonclick()