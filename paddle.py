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

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def edge_distance(self, other_turtle):
        self_wid, self_len, _ = self.shapesize()
        other_wid, other_len, _ = other_turtle.shapesize()

        self_w = self_len * 20
        self_h = self_wid * 20
        other_w = other_len * 20
        other_h = other_wid * 20

        dx = max(0, abs(self.xcor() - other_turtle.xcor()) - (self_w + other_w) / 2)
        dy = max(0, abs(self.ycor() - other_turtle.ycor()) - (self_h + other_h) / 2)

        if dx == 0 and dy == 0:
            return 0

        import math
        return math.sqrt(dx ** 2 + dy ** 2)
