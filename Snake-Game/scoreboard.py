from turtle import Turtle
ALIGN =  "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", "r") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)


