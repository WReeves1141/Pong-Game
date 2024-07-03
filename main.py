from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=820, height=620)
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    # border testing
    tim = Turtle()
    tim.shape("classic")
    tim.color("white")
    tim.penup()
    tim.setposition(-400, 300)
    tim.pendown()
    for i in range(2):
        tim.forward(800)
        tim.right(90)
        tim.forward(600)
        tim.right(90)
    tim.hideturtle()

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or \
            ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.left_point()

    if ball.ycor() < -380:
        ball.reset_position()
        score.right_point()

screen.exitonclick()
