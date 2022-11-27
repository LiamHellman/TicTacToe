# ChessBoard
__doc__ = """


    A8  B8  C8  D8  E8  F8  G8  H8
    A7  B7  C7  D7  E7  F7  G7  H7
    A6  B6  C6  D6  E6  F6  G6  H6
    A5  B5  C5  D5  E5  F5  G5  H5
    A4  B4  C4  D4  E4  F4  G4  H4
    A3  B3  C3  D3  E3  F3  G3  H3
    A2  B2  C2  D2  E2  F2  G2  H2
    A1  B1  C1  D1  E1  F1  G1  H1 

    0,7  1,7  2,7  3,7  4,7  5,7  6,7  7,7 
    0,6  1,6  2,6  3,6  4,6  5,6  6,6  7,6 
    0,5  1,5  2,5  3,5  4,5  5,5  6,5  7,5 
    0,4  1,4  2,4  3,4  4,4  5,4  6,4  7,4 
    0,3  1,3  2,3  3,3  4,3  5,3  6,3  7,3 
    0,2  1,2  2,2  3,2  4,2  5,2  6,2  7,2 
    0,0  1,1  2,1  3,1  4,1  5,1  6,1  7,1 
    0,0  1,0  2,0  3,0  4,0  5,0  6,0  7,0 

    Movement:

        Pawn = +1y White or -1y Black unless eating then diagonal
        Knight = (+2y +1x) or (+2y -1x) or (-2y +1x) or (-2y -1x) or (+2x +1y) or (+2x -1y) or (-2x +1y) or (-2x -1y)
        Rook = (+ 1x to 8x) or (- 1x to 8x) or (+ 1y to 8y) or (- 1y to 8y)
        Bishop = (+1 to 8x +1 to 8y) or (+1 to 8x -1 to 8y) or (+1 to 8y -1 to 8x) or (-1 to 8y -1 to 8x)
        Queen = (Bishop and Rook)
        King =  (+1x +1y) or (+1x -1y) or (-1x +1y) or (-1x -1y) or (+1x) or (-1x) or (+1y) or (-1y)


"""

#Variable
#PlayerWhite, PlayerBlack

#def pieces color + piece

#x,y moving on 8x8 grid while not going negative


