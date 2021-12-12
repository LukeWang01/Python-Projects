from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-500, 500)
        self.update_score()
        self.leve_num = 1

    def update_score(self):
        self.clear()
        self.leve_num += 1
        self.write(f"Leve {self.leve_num}:", align="left", font=FONT)

    def reset_score(self):
        self.clear()
        self.leve_num = 1



