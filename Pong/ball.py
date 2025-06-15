from turtle import Turtle
from random import uniform,randint


class Ball(Turtle):
    SPEED = 1
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.spawn((0, 0))

    def move(self):
        self.forward(Ball.SPEED)
    def wall_bounce(self):
        new_heading = -1*self.heading()
        self.setheading(new_heading)
        Ball.SPEED += 0.1

    def paddle_bounce(self):
        new_heading = 180 - 1*self.heading()
        self.setheading(new_heading)
        Ball.SPEED += 0.1

    def spawn(self,position):
        Ball.SPEED = 1.1
        rand = randint(0, 3)
        if rand == 0:
            angle = uniform(20, 50)
        elif rand == 1:
            angle = uniform(130, 160)
        elif rand == 2:
            angle = uniform(200, 230)
        else:
            angle = uniform(310, 340)
        self.goto(position)
        self.setheading(angle)
