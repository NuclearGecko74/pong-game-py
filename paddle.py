from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
