from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment_1 = Turtle("square")
        segment_1.shapesize(1, 1)
        segment_1.color("white")
        segment_1.penup()
        segment_1.goto(position)
        self.segments.append(segment_1)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            n_x = self.segments[seg_num - 1].xcor()
            n_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(n_x, n_y)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

