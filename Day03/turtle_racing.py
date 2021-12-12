from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)


def backward():
    t.backward(10)


def turn_left():
    new_heading = t.heading() + 10
    t.setheading(new_heading)


def turn_right():
    new_heading = t.heading() - 10
    t.setheading(new_heading)


def clear():
    t.penup()
    t.clear()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()

