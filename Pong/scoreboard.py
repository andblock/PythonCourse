from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier',24,'bold')


class Scoreboard(Turtle):
    player_num = 0
    score = 0

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-30 * (-1) ** Scoreboard.player_num, 250)
        self.keep_score()
        Scoreboard.player_num += 1
        if Scoreboard.player_num == 1:
            self.center()

    def keep_score(self):
        self.write(arg=f"{self.score}", move=False, align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.keep_score()

    def center(self):
        center = Turtle()
        center.hideturtle()
        center.penup()
        center.color("white")
        center.pensize(3)
        center.goto(0,-275)
        for x in range (0,9):
            if x == 0 or x == 8:
                center.pendown()
                center.goto(0,center.ycor()+17.5)
                center.penup()
                center.goto(0,center.ycor()+35)
            else:
                center.pendown()
                center.goto(0,center.ycor() + 35)
                center.penup()
                center.goto(0,center.ycor()+35)
