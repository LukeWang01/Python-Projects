import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.update()

player1 = Player()
screen.listen()
screen.onkey(player1.move_forward, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()
