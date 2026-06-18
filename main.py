import time

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

# Set up main screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800, 600)
screen.tracer(0)

# Set up paddles and set up ball
left_paddle = Paddle()
right_paddle = Paddle()

left_paddle.goto(-350, 0)
right_paddle.goto(350, 0)
screen.update()

ball = Ball()

# Set up events
screen.listen()
screen.onkeypress(key="w", fun=left_paddle.go_up)
screen.onkeypress(key="s", fun=left_paddle.go_down)
screen.onkeypress(key="Up", fun=right_paddle.go_up)
screen.onkeypress(key="Down", fun=right_paddle.go_down)

# Game Loop
running = True
while running:
    screen.update()
    time.sleep(0.016)

    ball.move()

    if left_paddle.edge_distance(ball) < 0.01 or right_paddle.edge_distance(ball) < 0.01:
        ball.bounce()

screen.exitonclick()
