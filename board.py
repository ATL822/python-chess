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
        row = []
        dims = (100, 100)
        for rowNum in range(0,8):
            for colNum in range(0,8):
                pos = (colNum, rowNum)
                row.append(Square.BoardSquare(determineSquareColor(colNum, rowNum), pos, dims))
            self.squares.append(row)
            row = []

    def __str__(self):
        for row in self.squares:
            for square in row:
                print(square)
        return '\n'
