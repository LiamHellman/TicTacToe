__doc__ - """

    (0)(1)(2)
    (3)(4)(5)
    (6)(7)(8)

"""
winState = False

board = [
    [1,1,1]
    [1,1,1]
    [1,1,1]
]


#row
if board[0] == board[1] == board[2]:
    winState = True
if board[3] == board[4] == board[5]:
    winState = True
if board[6] == board[7] == board[8]:
    winState = True
#collumn
if board[0] == board[3] == board[6]:
    winState = True
if board[1] == board[4] == board[7]:
    winState = True
if board[2] == board[5] == board[8]:
    winState = True
#diagonal
if board[0] == board[4] == board[8]:
    winState = True
if board[2] == board[4] == board[6]:
    winState = True
