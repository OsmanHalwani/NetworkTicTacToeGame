import socket
from tkinter import *
from tkinter import font
import time
xWins = 0
oWins = 0

# connecting to host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP Protocal declaring socket object
s.connect((socket.gethostname(), 3456)) # change socket.gethostname() to the ip address of the server
playerNum = s.recv(1024).decode("utf-8")


# this method sends the input of the user to the server and the server sends back the letter to be placed
def sendInput(i):

    s.send((bytes(str(i), "utf-8")))
    # getting whole String with X or O and pos
    letter = s.recv(1024).decode("utf-8")
    # spliting up the two
    pos = letter[len(letter) - 1]
    letter = letter.replace(pos, "")

    buttons[int(pos)]['text'] = letter

    for i in range(0, 9):
        buttons[i]['state'] = 'disabled'
    #updating GUI
    UI.update()

    checkForWin(letter)

    update()


def checkForWin(letter):
    win = False # boolean to see if win




    #checking horizontal wins
    if buttons[0]['text'] == letter and buttons[1]['text'] == letter and buttons[2]['text'] == letter:
        print(letter," wins")
        win = True

    elif buttons[3]['text'] == letter and buttons[4]['text'] == letter and buttons[5]['text'] == letter:
        print(letter," wins")
        win = True
    elif buttons[6]['text'] == letter and buttons[7]['text'] == letter and buttons[8]['text'] == letter:
        print(letter," wins")
        win = True
    #checking vertical wins
    elif buttons[0]['text'] == letter and buttons[3]['text'] == letter and buttons[6]['text'] == letter:
        print(letter, " wins")
        win = True
    elif buttons[1]['text'] == letter and buttons[4]['text'] == letter and buttons[7]['text'] == letter:
        print(letter, " wins")
        win = True
    elif buttons[1]['text'] == letter and buttons[4]['text'] == letter and buttons[7]['text'] == letter:
        print(letter, " wins")
        win = True
    elif buttons[2]['text'] == letter and buttons[5]['text'] == letter and buttons[8]['text'] == letter:
        print(letter, " wins")
        win = True
    #checking diagonal wins

    elif buttons[0]['text'] == letter and buttons[4]['text'] == letter and buttons[8]['text'] == letter:
        print(letter, " wins")
        win = True

    elif buttons[2]['text'] == letter and buttons[4]['text'] == letter and buttons[6]['text'] == letter:
        print(letter, " wins")
        win = True

    else:
        counter = 0
        for i in buttons:
            if i["text"] != "":
                counter+=1
            if counter == 9: # we have a tie
                break
        if counter == 9:
            for i in buttons:  # reset game
                i["text"] = ""
                i['state'] = "normal"



    if win: # when we have a win do this
        global xWins
        global oWins
        if letter == 'X':
            xWins+=1
        elif letter == 'O':
            oWins+=1
        scoreBoard['text'] = "ScoreBoard: \n X:" + str(xWins) + " "+"O:"+str(oWins)

        for i in buttons: #reset game
            i["text"] = ""
            i['state'] = "normal"

    i

def update():

    letter = s.recv(1024).decode("utf-8")
    # spliting up the two
    pos = letter[len(letter) - 1]
    letter = letter.replace(pos, "")


    buttons[int(pos)]['text'] = letter


    for i in range(0, 9):
        if buttons[i]["text"] == "":
            buttons[i]['state'] = 'normal'
    UI.update()
    checkForWin(letter)



UI = Tk()
buttons = []
times = font.Font(family='TimesNewRoman', size=20, weight='bold')

# running loop to set a 3x3 grid for game
for i in range(1, 4):

    for j in range(1, 4):
        button = Button(UI, text="", width=15, height=10)

        button['font'] = times
        buttons.append(button)
        button.grid(row=i, column=j)

scoreBoard = Label(UI,text ="ScoreBoard: \n X:" + str(xWins) + " "+"O:"+str(oWins),width = 15,height =15)
scoreBoard.grid(row = 1 , column = 4)





# this code below will send the correct coordinates of the button clicked by the player to the server
buttons[0]['command'] = lambda: sendInput(0)
buttons[1]['command'] = lambda: sendInput(1)
buttons[2]['command'] = lambda: sendInput(2)
buttons[3]['command'] = lambda: sendInput(3)
buttons[4]['command'] = lambda: sendInput(4)
buttons[5]['command'] = lambda: sendInput(5)
buttons[6]['command'] = lambda: sendInput(6)
buttons[7]['command'] = lambda: sendInput(7)
buttons[8]['command'] = lambda: sendInput(8)

if playerNum == "player2":
    for i in range(0, 9):
        buttons[i]['state'] = 'disabled'

    UI.update()
    update()

UI.mainloop()





