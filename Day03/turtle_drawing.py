import random
import turtle as t

# Random Walk

lt = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


lt.shape("turtle")
colors = ["red", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
          "SeaGreen"]
directions = [0, 90, 180, 270]
lt.pensize(5)
lt.speed("fastest")


for i in range(200):
    lt.color(random_color())
    lt.forward(20)
    lt.right(random.choice(directions))

# set screen
screen = t.Screen()
screen.exitonclick()

