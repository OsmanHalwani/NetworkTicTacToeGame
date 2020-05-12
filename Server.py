import socket
board = [["-","-","-"],["-","-","-"],["-","-","-"]]
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # TCP Protocal declaring socket object
s.bind((socket.gethostname(),3456))
s.listen(5) #socket needs to listen
#player 1 has joined
clinetsocket, address = s.accept()
clinetsocket2 , address = s.accept() # player 2 has joined

clinetsocket.send(((bytes(str("player1"), "utf-8"))))
clinetsocket2.send(((bytes(str("player2"), "utf-8"))))

# send the new board method
def sendNewBoard(letter,pos):
    #checking position to see what needs to be sent
    if pos == '0':
        board[0][0]=letter

        clinetsocket.send(bytes(letter+ pos,"utf-8"))
        clinetsocket2.send(bytes(letter + pos,"utf-8"))

    elif pos == '1':
        board[0][1] = letter

        clinetsocket.send(bytes(letter + pos, "utf-8"))
        clinetsocket2.send(bytes(letter + pos, "utf-8"))

    elif pos == '2':
        board[0][2] = letter

        clinetsocket.send(bytes(letter + pos, "utf-8"))
        clinetsocket2.send(bytes(letter + pos, "utf-8"))

    elif pos == '3':
        board[1][0] = letter

        clinetsocket.send(bytes(letter + pos, "utf-8"))
        clinetsocket2.send(bytes(letter + pos, "utf-8"))

    elif pos == '4':
        board[1][1] = letter

        clinetsocket.send(bytes(letter + pos, "utf-8"))
        clinetsocket2.send(bytes(letter + pos, "utf-8"))

    elif pos == '5':
        board[1][2] = letter

        clinetsocket.send(bytes(letter + pos, "utf-8"))
        clinetsocket2.send(bytes(letter + pos, "utf-8"))


    elif pos == '6':
        board[2][0] = letter

        clinetsocket.send(bytes(letter + pos, "utf-8"))
        clinetsocket2.send(bytes(letter + pos, "utf-8"))

    elif pos == '7':
        board[2][1] = letter

        clinetsocket.send(bytes(letter + pos, "utf-8"))
        clinetsocket2.send(bytes(letter + pos, "utf-8"))

    elif pos == '8':
        board[2][2] = letter

        clinetsocket.send(bytes(letter + pos, "utf-8"))
        clinetsocket2.send(bytes(letter + pos, "utf-8"))


while True:


    player1Move = clinetsocket.recv(32).decode("utf-8")# getting player one's input
    sendNewBoard("X",player1Move)
    player2Move = clinetsocket2.recv(32).decode(("utf-8"))
    sendNewBoard("O", player2Move)
