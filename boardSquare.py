class BoardSquare():
    color = (0,0,0)
    occupied = False
    pos = (0,0)
    dims = (100,100)

    def __init__(self, color : tuple, pos : tuple, dims : tuple):
        self.color = color
        self.occupied = False
        self.pos = pos
        self.dims = dims

    def __str__(self):
        return f'Square at: {self.pos} -- Color: {self.color} -- Occupied: {self.occupied}'

    def isOccupied(self):
        return self.occupied
    
    def setOccupied(self, state : bool):
        self.occupied = state

    def setColor(self, color : str):
        self.color = color
