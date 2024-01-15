from piece import Piece
from random import random

class Board():
    def __init__(self, size, bomb_probability):
        self.size = size
        self.bomb_probability = bomb_probability
        self.lost = False
        self.num_uncoverd = 0
        self.num_clicked = 0
        self.setBoard()

    def setBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                is_bomb = random() < self.bomb_probability
                if(not is_bomb):
                    self.num_uncoverd += 1
                piece = Piece(is_bomb)
                row.append(piece)
            self.board.append(row)
        self.setNeighbors()

    def setNeighbors(self):
        """
        Sets the neighbors of each piece on the board.

        Parameters:
            row (int): The row of the piece.
            col (int): The column of the piece.
            piece (Piece): The piece.
            neighbors (list): The list of neighbors.
            
        """
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.getPiece(row, col)
                neighbors = self.getNeighbors((row, col))
                piece.setNeighbors(neighbors)

    def getNeighbors(self, pos):
        """
        Returns a list of the neighbors of the piece at pos.

        Parameters:
            pos (tuple): The position of the piece.
            neighbors (list): The list of neighbors.
            outOfBounds (bool): Whether or not the piece is out of bounds.
            
        Returns:
            list: The list of neighbors.
        """
        neighbors = []
        for row in range(pos[0] - 1, pos[0] + 2):
            for col in range(pos[1] - 1, pos[1] + 2):
                outOfBounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                outOfBounds = outOfBounds or (row == pos[0] and col == pos[1])
                if outOfBounds:
                    continue
                neighbors.append(self.getPiece(row, col))
        return neighbors

    def getSize(self):
        return self.size
    
    def getPiece(self, row, col):
        return self.board[row][col]
    
    def handleMouseClick(self, piece, flag):
        if(piece.getClicked() or (not flag and piece.getFlagged())):
            return
        
        if (flag):
            piece.toggleFlag()
            return
        
        piece.click()

        if (piece.getIsBomb()):
            self.lost = True
            return
        
        self.num_clicked += 1

        if (piece.getNumAround() != 0):
            return
        for neighbor in piece.getNeighbors():
            if (not neighbor.getIsBomb() and not neighbor.getClicked()):
                self.handleMouseClick(neighbor, False)
        
    def getWon(self):
        return self.num_uncoverd == self.num_clicked and not self.lost
    
    def getLost(self):
        return self.lost
    
    def setLost(self, lost):
        self.lost = lost