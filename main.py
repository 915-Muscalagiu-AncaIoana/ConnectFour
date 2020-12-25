from model.board import Board
from model.validators import InputValidator, MoveValidator
from model.strategy import StrategyAI
from model.player import Computer, Human
from service.game import Game
from ui.ui import Ui
from gui.gui import GUI

board = Board(6, 7)
strategy = StrategyAI()
human = Human(1)
computer = Computer(2, strategy)
validator_input = InputValidator()
validator_move = MoveValidator()
game = Game(board, computer, human, validator_move)
ui = Ui(game,validator_input)
ui.start()
# gui = GUI(100, 7, 6, game,validator_move)
# gui.start()
