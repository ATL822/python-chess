class Peice():
    def __init__(self, active=False, color='white', pieceType='pawn', validMoves=[], pos=(0,0)) -> None:
        self.active = active
        self.color = color
        self.pieceType = pieceType
        self.validMoves = validMoves
        self.pos = pos
        