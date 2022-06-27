from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " Turn"))
            elif check_winner() is True:
                label.config(text=(players[0] + " Wins"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")
        else:

            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " Turn"))

            elif check_winner() is True:
                label.config(text=(players[1] + " Wins"))

            elif check_winner() == "Tie!":
                label.config(text="Tie!")

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text']== buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="red")
            buttons[row][1].config(bg="red")
            buttons[row][2].config(bg="red")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text']== buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="yellow")
        buttons[1][1].config(bg="yellow")
        buttons[2][2].config(bg="yellow")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="blue")
        buttons[1][1].config(bg="blue")
        buttons[2][0].config(bg="blue")
        return True

    elif empy_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(fg="blue")
        return "Tie!"
    else:
        return False


def empy_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False

    else:
        return True

def new_game():
    global player
    player = random.choice(players)

    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

window = Tk()
window.title("Tic-Tac-Toe")

window_width = 1000
window_height = 800
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")



players = ["x", "o"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " turn", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="restart", font=("consolas", 20), command=new_game)
reset_button.pack(side=TOP)

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("consolas", 40), width=5, height=2, command= lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()

