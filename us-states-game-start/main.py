from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. State Game")
img = "blank_states_img.gif"
screen.addshape(img)

usa_map = Turtle()
usa_map.shape(img)

state_date = pandas.read_csv("50_states.csv")

state_name = state_date.state.to_list()
guessed_state = []

all_state_guessed = False
while len(guessed_state) < 50:
    user_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="State Name: ")
    user_state = user_state.title()

    if user_state == "Exit":
        missing_state = []
        for state in state_name:
            if state not in guessed_state:
                missing_state.append(state)
        missed_data = pandas.DataFrame(missing_state)
        missed_data.to_csv("missed_data.csv")
        break

    if user_state in state_name:
        state_row = state_date[state_date.state == user_state]
        x_axis = int(state_row.x)
        y_axis = int(state_row.y)
        print_state = Turtle()
        print_state.penup()
        print_state.hideturtle()
        print_state.goto(x_axis, y_axis)
        print_state.write(f"{user_state}", align="left", font=("Arial", 8, "normal"))
        guessed_state.append(user_state)

