from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=1000, height=800)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y = -100

for i in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(x= -480, y= y)
    y += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for i in all_turtles:
        if i.xcor() > 470:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
               print(f"You've lost! The {winning_color} turtle is the winner!") 
            
        rand_distance = random.randint(0, 10)
        i.forward(rand_distance)

screen.exitonclick()