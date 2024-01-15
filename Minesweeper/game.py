import pygame
import os
from time import sleep

class Game():
    def __init__(self, board, screen_size, timer):
        self.board = board
        self.screen_size = screen_size
        self.piece_size = (self.screen_size[0] // self.board.size[0], (self.screen_size[1] - 100) // self.board.size[1])
        self.time_now = 0
        self.timer = timer
        self.loadImages()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Minesweeper")
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(60)
            self.time_now = pygame.time.get_ticks() // 1000

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleMouseClick(pos, rightClick)
            self.draw()
            pygame.display.flip()

            # Check the state of the game ( win or lose )
            if(self.time_now == self.timer and self.timer != 0):
                self.board.setLost(True)
            if(self.board.getWon()):
                sound = pygame.mixer.Sound("./Minesweeper/win.mp3")
                sound.play()
                sleep(5)
                running = False
            if(self.board.getLost()):
                sound = pygame.mixer.Sound("./Minesweeper/lost.mp3")
                sound.play()
                self.drawLost()
                sleep(5)
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

        # Timer
        font = pygame.font.Font('freesansbold.ttf', 32)
        timer_text = font.render(f"Time: {self.time_now}", True, (255, 255, 255))    
        pygame.draw.rect(self.screen, (0, 0, 0), (10, self.screen_size[1] - 50, 150, 50))
        self.screen.blit(timer_text, (10, self.screen_size[1] - 50))

        # timer
        font = pygame.font.Font('freesansbold.ttf', 32)
        timer_text = font.render(f"Time Limit: {self.timer}", True, (255, 255, 255))
        pygame.draw.rect(self.screen, (0, 0, 0), (self.screen_size[0] - 200, self.screen_size[1] - 50, 175, 50))
        self.screen.blit(timer_text, (self.screen_size[0] - 275, self.screen_size[1] - 50))

            
    def drawLost(self):
        for row in range(self.board.getSize()[0]):
                for col in range(self.board.getSize()[1]):
                    piece = self.board.getPiece(row, col)
                    if(piece.getIsBomb()):
                        image = self.getImage(piece)
                        self.screen.blit(image, (col * self.piece_size[0], row * self.piece_size[1]))

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
        """
        Returns the image of the piece.

        Parameters:
            string (str): The name of the image.
            piece (Piece): The piece.

        Returns:
            pygame.Surface: The image of the piece.
        """
        string = None
        if piece.getClicked():
            string = "bomb-at-clicked-block" if piece.getIsBomb() else str(piece.getNumAround())
        else:
            string = "flag" if piece.getFlagged() else "empty-block"
            if piece.getIsBomb() and self.board.getLost():
                string = "unclicked-bomb"
        return self.images[string]
    
    def handleMouseClick(self, pos, rightClick):
        """
        Handles the mouse click.

        Parameters:
            pos (tuple): The position of the mouse.
            index (tuple): The index of the piece.
            piece (Piece): The piece.
        """
        if(self.board.getLost()):
            return
        index = (pos[1] // self.piece_size[1], pos[0] // self.piece_size[0])
        piece = self.board.getPiece(index[0], index[1])
        self.board.handleMouseClick(piece, rightClick)

    def getTimeNow(self):
        return self.time_now
    
    def getTimer(self):
        return self.timer