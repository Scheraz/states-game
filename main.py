import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")
state_list = data["state"].to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


answered = []
score = 0

while len(answered) < len(state_list):
    answer_state = screen.textinput(title=f"Guess the state {score}/{len(state_list)}", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state in state_list and answer_state not in answered:
        answered.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        score += 1
        user_data = data[data.state == answer_state]
        t.goto(user_data.x.item(), user_data.y.item())
        t.write(user_data.state.item())

missed_states = []
for i in state_list:
    if i not in answered:
        missed_states.append(i)

pd.DataFrame(missed_states,columns=["Missed States"]).to_csv("States to learn")