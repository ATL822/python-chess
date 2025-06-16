import boardSquare as Square

def determineSquareColor(col, row):
    if col % 2 == 0:
        if row % 2 == 0:
            squareColor = (140,123,74)
        else:
            squareColor = (94,67,40)
    else:
        if row % 2 == 1:
            squareColor = (140,123,74)
        else:
            squareColor = (94,67,40)
    return squareColor

class Board():
    def __init__(self):
        self.squares = []
        dims = (100, 100)
        for squareRow in range(0,8):
            for squareCol in range(0,8):
                pos = (squareCol, squareRow)
                self.squares.append(Square.BoardSquare(determineSquareColor(squareCol, squareRow), pos, dims))

    def __str__(self):
        for square in self.squares:
            print(square)
        return '\n'
