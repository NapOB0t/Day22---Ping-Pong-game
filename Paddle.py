from turtle import Turtle


class Paddle(Turtle):
    def __init__(self , distance):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.resizemode("user")
        self.shapesize(5, 1, 1)
        self.goto(distance)

    def go_up(self):

        y_up = self.ycor() + 30
        self.goto(self.xcor(), y_up)

    def go_down(self):
        y_down = self.ycor() - 30
        self.goto(self.xcor(), y_down)

