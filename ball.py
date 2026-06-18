from enum import Enum
from random import choice
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.initial_speed = [2, 2]
        self.current_speed = self.initial_speed

        self.setup()

    def setup(self):
        self.penup()
        self.color("white")
        self.shape("circle")
        self.current_speed[0] *= choice([1, -1])
        self.current_speed[1] *= choice([1, -1])

    def move(self):
        new_x = self.xcor() + self.current_speed[0]
        new_y = self.ycor() + self.current_speed[1]

        self.goto(new_x, new_y)

        hit_wall = new_y > 290 or new_y < -290
        if hit_wall:
            self.current_speed[1] *= -1

    def bounce(self):
        self.current_speed[0] *= -1.1
        self.current_speed[1] *= -1
