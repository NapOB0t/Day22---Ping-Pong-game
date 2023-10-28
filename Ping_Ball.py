from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.goto(0, 0)
        self.movey = random.randint(-20,20)
        self.movex = random.randint(-20,20)

    def move(self):
        x = self.xcor() + self.movex
        y = self.ycor() + self.movey
        self.goto(x, y)

    def bouncewall(self):
        self.movey *= -1

    def bouncepaddle(self):
        self.movey *= -1
        self.movex *= -1







