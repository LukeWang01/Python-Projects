import time
from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for i in starting_position:
    segment_1 = Turtle("square")
    segment_1.color("white")
    segment_1.penup()
    segment_1.goto(i)
    segments.append(segment_1)

screen.update()  # just like animation, one update is one frame

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments), 0, -1):
        n_x = segments[seg_num - 1].xcor()
        n_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(n_x, n_y)
    segments[0].forward(20)


screen.exitonclick()
