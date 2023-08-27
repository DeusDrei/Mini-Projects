from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        a = Turtle(shape="square")
        a.penup()
        a.color("green")
        a.goto(position)
        self.snake_body.append(a)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())
    
    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.head.forward(DISTANCE)
    
    def reset(self):
        for i in self.snake_body:
            i.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)