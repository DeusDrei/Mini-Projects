from turtle import Screen
import time
from snakes import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.down, key="Down")

is_on = True

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for i in snake.snake_body[1:]:
        if snake.head.distance(i) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
