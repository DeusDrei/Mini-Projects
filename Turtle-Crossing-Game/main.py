import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

alain = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=alain.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.new_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(alain) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    if alain.at_finish_line():
        alain.reset()
        car_manager.move_faster()
        scoreboard.add_level()


screen.exitonclick()