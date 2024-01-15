from game import Game
from board import Board

size = (9, 9)
bombProb = 0.1
#set the time limit in seconds (0 for no time limit)
timer = 5
board = Board(size, bombProb)
screenSize = (800, 900)
game = Game(board, screenSize, timer)
game.run()