from enum import Enum
from random import choice
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed_x = choice([1, 2])
        self.speed_y = choice([1,2,3])

        self.setup()

    def setup(self):
        self.penup()
        self.color("white")
        self.shape("circle")
        self.set_random_speed()

    def move(self):
        new_x = self.xcor() + self.speed_x
        new_y = self.ycor() + self.speed_y

        self.goto(new_x, new_y)

        hit_wall = new_y > 290 or new_y < -290
        if hit_wall:
            self.speed_y *= -1

    def bounce(self):
        self.speed_x *= -1.1

    def reset_ball(self):
        self.speed_x = choice([1, 2])
        self.speed_y = choice([1, 2, 3])
        self.reset()
        self.setup()

    def set_random_speed(self):
        self.speed_x = choice([1, 2])
        self.speed_y = choice([1, 2, 3])