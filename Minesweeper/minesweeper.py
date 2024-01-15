from game import Game
from board import Board

size = (3, 3)
bombProb = 0.1
board = Board(size, bombProb)
screenSize = (800, 800)
game = Game(board, screenSize)
game.run()