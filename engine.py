

winState = False
turn = 0

board = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
]


#row
while winState == False or turn <10:
    turn = turn + 1

    turnX = input("Your xsign ")
    turnY = input("Your y sign ")


    if turn %2 == 0:
        board[turnX][turnY] == '0'
    if turn %2 != 0:
        board[turnX][turnY] == '0'

    print(board)

    #rows
    if board[0][0] == board[1][0] == board[2][0]:
        winState = True
    if board[0][1] == board[1][1] == board[2][1]:
        winState = True
    if board[0][2] == board[1][2] == board[2][2]:
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
