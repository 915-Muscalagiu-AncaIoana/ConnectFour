from model.board import Board
from model.validators import InputValidator, MoveValidator
from model.strategy import StrategyAI
from model.player import Computer, Human
from service.game import Game
from ui.ui import Ui
from gui.gui import GUI


class AppCoord:
    @staticmethod
    def start_program():

        board = Board(6, 7)
        strategy = StrategyAI()
        human = Human(1)
        computer = Computer(2, strategy)
        validator_input = InputValidator()
        validator_move = MoveValidator()
        game = Game(board, computer, human, validator_move)
        print('Please choose the type of interface you want:')

        while True:
            option = input('Interface: ')
            option.strip()
            if option == 'ui':
                ui = Ui(game, validator_input)
                ui.start()
                break
            elif option == 'gui':
                gui = GUI(100, 7, 6, game, validator_move)
                gui.start()
                break
            else:
                print('Incorrect option, the interface must be a ui or a gui.')
