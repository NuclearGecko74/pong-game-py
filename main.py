from turtle import Turtle, Screen
from paddle import Paddle

# Set up main screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800, 600)
screen.tracer(0)

# Set up paddles
left_paddle = Paddle()
right_paddle = Paddle()

left_paddle.goto(-350, 0)
right_paddle.goto(350, 0)
screen.update()

screen.exitonclick()
