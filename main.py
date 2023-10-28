from turtle import Screen
from Paddle import Paddle
from Ping_Ball import Ball
from scoreboard import Score
import time
#Screen configuration

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("MBN Ping Pong Game")
screen.tracer(0)# removes all animation so that it is not visible at the initial state of the game


#Paddles Configuration
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

#Ball object Configuration

ball = Ball()

#Scoreboard object configuration

score = Score()
game_is_on = True

while game_is_on:
    time.sleep(0.15)
    screen.update()
    ball.move()
    score.updatescore()
    # make the ball bounce off the upper wall and lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncewall()

    # make the ball bounce after it collides with a paddle
    if ball.distance(r_paddle) <= 50 or ball.distance(l_paddle) <= 50:
        ball.bouncepaddle()
        score.addscore()


    # making the game end if the ball goes past the boundaries
    if ball.xcor() > 400 or ball.xcor() < -400:
        score.gameover()
        game_is_on = False












screen.exitonclick()
