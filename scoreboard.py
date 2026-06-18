from turtle import Turtle


def draw_dashed_line():
    dashed_line = Turtle()
    dashed_line.penup()
    dashed_line.goto(0, 290)
    dashed_line.color("white")
    dashed_line.right(90)
    dashed_line.hideturtle()
    while dashed_line.ycor() > -290:
        dashed_line.pendown()
        dashed_line.forward(10)
        dashed_line.penup()
        dashed_line.forward(10)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0

        draw_dashed_line()
        self.setup()

    def setup(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 220)
        self.update_scoreboard()

    def update_scoreboard(self):
        text = f"{self.left_score}    {self.right_score}"
        font_score = ('Arial', 50, 'normal')

        self.clear()
        self.write(text, align='center', font=font_score)

    def increase_left_score(self):
        self.left_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.right_score += 1
        self.update_scoreboard()
