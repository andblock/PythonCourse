from turtle import Turtle


class Wall(Turtle):

    wall_num = 0
    WALL_DISTANCE = 295
    CHROME = 10
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("orange")
        self.shapesize(stretch_wid=0.5,stretch_len=40)
        self.penup()
        self.goto(x=0,y=Wall.WALL_DISTANCE*(-1)**Wall.wall_num + Wall.CHROME*Wall.wall_num)
        Wall.wall_num += 1
