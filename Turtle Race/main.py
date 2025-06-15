from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def create_turtles():
    """Creates a group of six turtles of different colors."""
    turtle_list = []
    for turtle_color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(turtle_color)
        new_turtle.penup()
        turtle_list.append(new_turtle)
    return turtle_list


# def exit_race():
#     global race_on
#     race_on = False
#     screen.bye()


screen.tracer(0)
finline = Turtle(shape="square")
finline.color("gray")
finline.shapesize(stretch_wid=100,stretch_len=1.6)
finline.penup()
finline.goto(x=230,y=0)

turtles = create_turtles()
for turtle in turtles:
    value = turtles.index(turtle)
    if value % 2 == 0:
        turtle.goto(x=-230,y=30*(1+value))
    else:
        turtle.goto(x=-230,y=-30-30*(value-1))
screen.update()
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the face? Enter a color.")
while user_bet.lower() not in colors:
    user_bet = screen.textinput(title="Make your bet",prompt="Invalid input. Enter valid turtle color.")

def turtle_race():
    global keep_racing
    rand_turtle = randint(0,5)
    turtles[rand_turtle].forward(0.5)
    for turtle in turtles:
        if turtle.xcor() > 220:
            turtle_number = turtles.index(turtle)
            winning_color = colors[turtle_number]
            screen.update()
            print(f"The {winning_color} turtle is the victor!")
            if user_bet == winning_color:
                print("YOU WIN!")
            else:
                print("YOU LOSE!")
            return
    screen.update()
    screen.ontimer(fun=turtle_race,t= 1)


if user_bet:
    turtle_race()

screen.onkey(fun=screen.bye, key="q")
screen.listen()
screen.mainloop()