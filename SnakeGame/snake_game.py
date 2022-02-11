import time
from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.update()  # just like animation, one update is one frame

snake1 = Snake()
screen.listen()
screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.left, "Left")
screen.onkey(snake1.right, "Right")

food = Food()
scoreboard = Scoreboard()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake1.move()

    # Get food
    if snake1.head.distance(food) < 15:
        food.refresh()
        snake1.extend()
        scoreboard.add_score()

    # Head to wall
    if snake1.head.xcor() > 280 or snake1.head.xcor() < -280 or snake1.head.ycor() > 280 or snake1.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Head to tail
    for segment in snake1.segments[1:]:
        if snake1.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

