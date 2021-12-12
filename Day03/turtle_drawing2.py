import random
import turtle as t
import colorgram

# Random Walk
colors = colorgram.extract('image.jpg', 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)


lt = t.Turtle()
t.colormode(255)

lt.penup()
lt.hideturtle()
lt.speed("fastest")
lt.setheading(255)
lt.forward(300)
lt.setheading(0)
num_dots = 100

for i in range(1, num_dots + 1):
    lt.pendown()
    lt.dot(20, random.choice(rgb_colors))
    lt.penup()
    lt.forward(50)
    lt.pendown()
    if i % 10 == 0:
        lt.penup()
        lt.setheading(90)
        lt.forward(50)
        lt.setheading(180)
        lt.forward(500)
        lt.setheading(0)


screen = t.Screen()
screen.exitonclick()
