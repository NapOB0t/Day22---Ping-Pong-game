from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(x=0, y=270)
        self.hideturtle()
        self.updatescore

    def updatescore(self):
        self.write(arg=f"Score : {self.score}", align="center", font="Arial")

    def addscore(self):
        self.score += 1
        self.clear()
        self.updatescore()

    def gameover(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over your final score is {self.score}", align="center", font="Arial")




