from game import Game
from board import Board

size = (9, 9)
bomb_probability = 0.05
#set the time limit in seconds (0 for no time limit)
timer = 0
board = Board(size, bomb_probability)
screenSize = (800, 900)
game = Game(board, screenSize, timer)
game.run()