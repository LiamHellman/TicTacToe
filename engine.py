import numpy as np

winState = False
turn = 0
board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


while winState == False and turn <10:
    turn = turn + 1

    turnX = input("Your xsign ")
    turnY = input("Your y sign ")


    if turn %2 == 0:
        board[int(turnX)][int(turnY)] = "O" 
    if turn %2 != 0:
        board[int(turnX)][int(turnY)] = "X"

    print(np.matrix(board))

    #rows
    if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        winState = True
    if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        winState = True
    if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        winState = True
    #collumn
    if board[0][0] == board[0][1] == board[0][2]:
        winState = True
    if board[1][0] == board[1][1] == board[1][2]:
        winState = True
    if board[2][0] == board[2][1] == board[2][2]:
        winState = True
    #diagonal
    if board[0][0] == board[1][1] == board[2][2]:
        winState = True
    if board[2][0] == board[1][1] == board[0][2]:
        winState = True

if turn == 10:
    print("tie")
elif turn % 2 == 0:
    print("O Win")
elif turn % 2 == 1:
    print("X Win")

