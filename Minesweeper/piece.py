class Piece():
    def __init__(self, isBomb):
        self.isBomb = isBomb
        self.flagged = False
        self.clicked = False

    def getIsBomb(self):
        return self.isBomb
    
    def getClicked(self):
        return self.clicked
    
    def getFlagged(self):
        return self.flagged
    
    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
        self.setNumAround()

    def getNeighbors(self):
        return self.neighbors

    def setNumAround(self):
        self.numAround = 0
        for piece in self.neighbors:
            if piece.getIsBomb():
                self.numAround += 1
    
    def getNumAround(self):
        return self.numAround
    
    def toggleFlag(self):
        self.flagged = not self.flagged

    def click(self):
        self.clicked = True
