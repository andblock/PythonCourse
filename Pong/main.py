from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from walls import Wall
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

p1_paddle = Paddle()
p2_paddle = Paddle()
p1_score = Scoreboard()
p2_score = Scoreboard()
upper_wall = Wall()
lower_wall = Wall()
ball = Ball()

screen.listen()
screen.onkey(p1_paddle.up,key="w")
screen.onkey(p1_paddle.down,key="s")
screen.onkey(p2_paddle.up,key="Up")
screen.onkey(p2_paddle.down,key="Down")


def play():
    #Detect collisions with walls
    if ball.ycor() <= -270 or ball.ycor() >= 280:
        ball.wall_bounce()
    #Detect collisions with left paddle
    if ball.distance(p1_paddle) < 60 and -350 > ball.xcor() > -355:
        ball.paddle_bounce()
    if ball.distance(p2_paddle) < 60 and 355 > ball.xcor() > 350:
        ball.paddle_bounce()
    if ball.xcor() > 400:
        p1_score.increase_score()
        ball.spawn((0, 0))
    if ball.xcor() < -400:
        p2_score.increase_score()
        ball.spawn((0,0))
    if p1_score:
        screen.update()
        ball.move()
        screen.update()
        screen.ontimer(play,1)
play()


















screen.mainloop()