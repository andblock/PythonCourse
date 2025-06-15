import turtle
import pandas

turtle_scribe = turtle.Turtle()

def write_at_location(x,y,text):
    turtle_scribe.hideturtle()
    turtle_scribe.penup()
    turtle_scribe.goto(x,y)
    turtle_scribe.write(text)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_names = states_data.state                    # Converts DataFrame to Series
all_states = states_names.to_list()                 # Converts Series to List
guessed_states = []
def play():

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state.title() == "Exit":
        unguessed_states = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(unguessed_states).to_csv("states_to_learn.csv", index=False)
        screen.bye()
        return
    # for state in states_names:
    if answer_state in all_states and answer_state not in guessed_states:
        # if state not in guessed_states:
        guessed_states.append(answer_state)
        xcoords = states_data.loc[states_data.state == answer_state,"x"].values[0]
        ycoords = states_data.loc[states_data.state == answer_state,"y"].values[0]
        write_at_location(xcoords,ycoords,answer_state)
    if len(guessed_states) < 50:
        screen.ontimer(play,100)
play()

screen.mainloop()