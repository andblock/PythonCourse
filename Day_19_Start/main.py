# _________________________________________TURTLE EVENT LISTENERS_______________________________________________________

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()
# Craft an Etch-A-Sketch App

move_up = False
move_down = False
move_left = False
move_right = False

def start_move_forward():
    global move_up
    move_up = True

def stop_move_forward():
    global move_up
    move_up = False

def start_move_backward():
    global move_down
    move_down = True

def stop_move_backward():
    global move_down
    move_down = False

def start_move_left():
    global move_left
    move_left = True

def stop_move_left():
    global move_left
    move_left = False

def start_move_right():
    global move_right
    move_right = True

def stop_move_right():
    global move_right
    move_right = False

def move():
    if move_left and move_up:
        tim.forward(10)
        tim.left(5)
    elif move_left and move_down:
        tim.backward(10)
        tim.left(5)
    elif move_right and move_up:
        tim.forward(10)
        tim.right(5)
    elif move_right and move_down:
        tim.backward(10)
        tim.right(5)
    elif move_up:
        tim.forward(10)
    elif move_down:
        tim.backward(10)
    elif move_left:
        tim.left(5)
    elif move_right:
        tim.right(5)
    screen.ontimer(fun=move,t=5)
move()
screen.onkeypress(fun=start_move_forward, key="Up")
screen.onkeypress(fun=start_move_backward, key="Down")
screen.onkeypress(fun=start_move_left, key="Left")
screen.onkeypress(fun=start_move_right, key="Right")
screen.onkeyrelease(fun=stop_move_forward, key="Up")
screen.onkeyrelease(fun=stop_move_backward, key="Down")
screen.onkeyrelease(fun=stop_move_left, key="Left")
screen.onkeyrelease(fun=stop_move_right, key="Right")

screen.onkey(fun=screen.bye,key="q")
screen.mainloop()