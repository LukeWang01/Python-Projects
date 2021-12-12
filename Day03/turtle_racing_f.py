import random
from turtle import Turtle, Screen

race_on = False
t = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? enter a color")
y_positions = [-70, -40, -10, 20, 50, 80]
colors = ["red", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
          "SeaGreen"]
all_turtles = []

for i in range(0, 6):

    lt = Turtle(shape="turtle")
    lt.penup()
    lt.color(colors[i])
    lt.goto(x=-230, y=y_positions[i])
    all_turtles.append(lt)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            race_on = False
            winning = turtle.pencolor()
            if winning == user_bet:
                print(f" You win! the {winning} turtle is the winner")
            else:
                print(f" You lost! the {winning} turtle is the winner")
        dis = random.randint(0, 10)
        turtle.forward(dis)


screen.exitonclick()
