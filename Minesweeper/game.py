import pygame
import os
from time import sleep

class Game():
    def __init__(self, board, screen_size):
        self.board = board
        self.screen_size = screen_size
        self.piece_size = (self.screen_size[0] // self.board.size[0], self.screen_size[1] // self.board.size[1])
        self.loadImages()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Minesweeper")
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleMouseClick(pos, rightClick)
            self.draw()
            pygame.display.flip()
            if(self.board.getWon()):
                sound = pygame.mixer.Sound("./Minesweeper/win.mp3")
                sound.play()
                sleep(5)
                running = False
            if(self.board.getLost()):
                sound = pygame.mixer.Sound("./Minesweeper/lost.mp3")
                sound.play()
                sleep(3)
                running = False
        pygame.quit()

    def draw(self):
        """
        Draws the board.

        Parameters:
            top_left (tuple): The top left corner of the board.
            row (int): The row of the piece.
            col (int): The column of the piece.
            piece (Piece): The piece.
            image (pygame.Surface): The image of the piece.
        """
        top_left = (0, 0)
        for row in range (self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece(row, col)
                image = self.getImage(piece)
                self.screen.blit(image,    top_left)
                top_left = top_left[0] + self.piece_size[0],   top_left[1]
            top_left = 0, top_left[1] + self.piece_size[1]

    def loadImages(self):
        """
        Loads the images for the pieces.

        Parameters:
            fileName (str): The name of the file.
            image (pygame.Surface): The image of the piece.

        """
        self.images = {}
        for fileName in os.listdir("Minesweeper/images"):
            if fileName.endswith(".png"):
                image = pygame.image.load(r"Minesweeper/images/" + fileName)
                image = pygame.transform.scale(image, self.piece_size)
                self.images[fileName.split(".")[0]] = image

    def getImage(self, piece):
        string = None
        if piece.getClicked():
            string = "bomb-at-clicked-block" if piece.getIsBomb() else str(piece.getNumAround())
        else:
            string = "flag" if piece.getFlagged() else "empty-block"
        return self.images[string]
    
    def handleMouseClick(self, pos, rightClick):
        if(self.board.getLost()):
            return
        index = (pos[1] // self.piece_size[1], pos[0] // self.piece_size[0])
        piece = self.board.getPiece(index[0], index[1])
        self.board.handleMouseClick(piece, rightClick)