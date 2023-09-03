from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
    
    def new_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(y=random_y, x=300)
            self.all_cars.append(car)
    
    def move_car(self):
        for i in self.all_cars:
            i.backward(self.car_speed)
        
    def move_faster(self):
        self.car_speed += MOVE_INCREMENT
    