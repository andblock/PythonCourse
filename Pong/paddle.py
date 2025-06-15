from turtle import Turtle


class Paddle(Turtle):
    pad_num = 0
    CHROME = 8
    WALL_DISTANCE = 370

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.setheading(90)
        # Second element compensates for window chrome being weighted to right side of window.
        self.goto(x=-self.WALL_DISTANCE*(-1)**self.pad_num - self.CHROME*self.pad_num,y=0)
        Paddle.pad_num += 1

    def up(self):
        self.forward(40)

    def down(self):
        self.backward(40)


