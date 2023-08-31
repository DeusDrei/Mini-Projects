from turtle import Screen
from pong import Pong
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_pong = Pong((350, 0))
l_pong = Pong((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_pong.move_up, key="Up")
screen.onkey(fun=r_pong.move_down, key="Down")
screen.onkey(fun=l_pong.move_up, key="w")
screen.onkey(fun=l_pong.move_down, key="s")

is_on = True
while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_pong) < 50 and ball.xcor() > 320 or ball.distance(l_pong) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Right Paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    # Left Paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
