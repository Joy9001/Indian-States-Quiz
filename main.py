import turtle
import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=628, height=746)
screen.title("Indian State Games")
image = "blank_indian_states.gif"
screen.addshape(image)

turtle.shape(image)

States_data = pandas.read_csv("States.csv")
States = States_data["state"].tolist()
Guessed_States = []
Missed_States = []
total = 36
guessed = 0
while guessed != total:
    user_input = screen.textinput(f"{guessed}/{total} GUESS THE STATE", "What's the next state?")
    user_input = user_input.title()
    Guessed_States.append(user_input)
    if user_input == "Exit":
        for s in States:
            if s not in Guessed_States:
                Missed_States.append(s)
        missed = pandas.DataFrame(Missed_States, columns=["States"])
        missed.to_csv("Missed_states.csv")
        break
    if user_input in States:
        index = States.index(user_input)
        guessed += 1
        state = Turtle()
        state.pu()
        state.hideturtle()
        xcor = int(States_data[States_data.state == States[index]].x.item())
        ycor = int(States_data[States_data.state == States[index]].y.item())
        state.setpos(xcor, ycor)
        state.write(user_input, align="center", font=('Arial', 8, 'normal'))

