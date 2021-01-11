import unittest
import texttable
from model.board import Board
from model.validators import InputValidator, MoveValidator, InputError, MoveError
from model.strategy import StrategyAI
from model.player import Computer, Human
from service.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        board1 = Board(6, 7)
        board2 = Board(6, 7)
        for col in range(7):
            board2.move_on_board(col, col % 2 + 1)
            board2.move_on_board(col, col % 2 + 1)
            board2.move_on_board(col, col % 2 + 1)

        for col in range(7):
            board2.move_on_board(col, (col+1) % 2 + 1)
            board2.move_on_board(col, (col + 1) % 2 + 1)
            board2.move_on_board(col, (col+1) % 2 + 1)

        strategy = StrategyAI()
        human = Human(1)
        computer = Computer(2, strategy)
        validator_move = MoveValidator()
        self._game1 = Game(board1, computer, human, validator_move)
        self._game2 = Game(board2, computer, human, validator_move)

    def test_check_game_over(self):
        self.assertEqual(self._game1.check_game_over(), False)
        self._game1.human_move(1)
        self._game1.human_move(1)
        self._game1.human_move(1)
        self._game1.human_move(1)
        self.assertEqual(self._game1.check_game_over(), True)
        self.assertEqual(self._game1.check_game_over(), True)

    def test_check_game_won(self):
        self.assertEqual(self._game1.check_game_won(), None)
        self._game1.computer_move()
        self._game1.computer_move()
        self._game1.computer_move()
        self._game1.computer_move()
        self.assertEqual(self._game1.check_game_won(),2)

    def test_check_game_draw(self):
        self._game2.check_game_draw()
        self.assertEqual(self._game2.get_game_state(),True)
        self._game1.check_game_draw()

    def test_human_move(self):
        self._game1.human_move(1)
        self.assertEqual(self._game1.get_cell_of_board(5,1),1)

    def test_computer_move(self):
        self._game1.computer_move()
        self.assertEqual(self._game1.get_cell_of_board(5, 3), 2)

    def test_get_board(self):
        table = self._game1.get_board()

    def test_get_winner(self):
        self._game1.human_move(1)
        self._game1.human_move(1)
        self._game1.human_move(1)
        self._game1.human_move(1)
        self.assertEqual(self._game1.get_winner(),1)





class Strategy(unittest.TestCase):
    def setUp(self):
        self._board = Board(6, 7)
        self._strategy = StrategyAI()

    def test_minimax(self):
        board1 = Board(6, 7)
        board2 = Board(6, 7)
        board1.move_on_board(1, 1)
        board1.move_on_board(2, 2)
        board1.move_on_board(3, 2)
        board1.move_on_board(1, 1)
        board1.move_on_board(1, 1)
        board1.move_on_board(4, 2)
        best_move = self._strategy.minimax(board1, 4, float("-inf"), float("inf"), True, 2,1)[0]
        self.assertEqual(best_move, 5)
        board2.move_on_board(1, 1)
        board2.move_on_board(1, 1)
        board2.move_on_board(0, 2)
        board2.move_on_board(0, 2)
        best_move = self._strategy.minimax(board2, 4, float("-inf"), float("inf"), True, 2,1)[0]
        self.assertEqual(best_move, 0)
        board3 = Board(6, 7)
        value = 1
        for col in range(7):
            board3.move_on_board(col, col % 2 + 1)
            board3.move_on_board(col, col % 2 + 1)
            board3.move_on_board(col, col % 2 + 1)

        for col in range(7):
            board3.move_on_board(col, (col+1) % 2 + 1)
            board3.move_on_board(col, (col + 1) % 2 + 1)
            board3.move_on_board(col, (col+1) % 2 + 1)
        best_move = self._strategy.minimax(board3, 4, float("-inf"), float("inf"), True, 2,1)[0]
        self.assertEqual(best_move, None)


class Player(unittest.TestCase):
    def setUp(self):
        self._board = Board(6, 7)
        self._human = Human(1)
        self._strategy = StrategyAI()
        self._computer = Computer(2, self._strategy)

    def test_human_move(self):
        self._human.human_move(self._board, 5, 0)
        self.assertEqual(self._board.get_certain_value(5, 0), 1)

    def test_computer_move(self):
        self._human.human_move(self._board, 5, 0)
        self._human.human_move(self._board, 4, 0)
        self._human.human_move(self._board, 3, 0)
        board = self._board
        self._computer.computer_move(board)
        self.assertEqual(self._board.get_certain_value(2, 0), 2)


class TestBoard(unittest.TestCase):
    def setUp(self):
        self._height = 6
        self._width = 7

    def test_create_board(self):
        board = Board(self._height, self._width)
        for row in range(self._height):
            for column in range(self._width):
                self.assertEqual(board.get_certain_value(row, column), 0)

    def test_move_on_board(self):
        board = Board(self._height, self._width)
        board.move_on_board(2, 1)
        for row in range(self._height):
            for column in range(self._width):
                if column == 2 and row == 5:
                    self.assertEqual(board.get_certain_value(row, column), 1)
                else:
                    self.assertEqual(board.get_certain_value(row, column), 0)

    def test_game_won(self):
        board = Board(self._height, self._width)
        self.assertEqual(None, board.game_won())
        for _ in range(4):
            board.move_on_board(2, 1)

        self.assertEqual(1, board.game_won())

        board = Board(self._height, self._width)
        for col in range(4):
            board.move_on_board(col, 2)

        self.assertEqual(2, board.game_won())

        board = Board(self._height, self._width)
        for index in range(4):
            for col in range(index, 4):
                board.move_on_board(col, (col - index) % 2 + 1)

        self.assertEqual(1, board.game_won())

        board = Board(self._height, self._width)
        for index in range(6, 2, -1):
            for col in range(index, 2, -1):
                board.move_on_board(col, (col - index - 1) % 2 + 1)

        self.assertEqual(2, board.game_won())

    def test_evaluate_window(self):
        board = Board(self._height, self._width)
        window = [1, 1, 1, 1]
        player = 1
        self.assertEqual(30000000, board.evaluate_window(window, player))
        window = [1, 1, 1, 0]
        self.assertEqual(150, board.evaluate_window(window, player))
        window = [1, 0, 0, 1]
        self.assertEqual(60, board.evaluate_window(window, player))
        window = [2, 2, 0, 2]
        self.assertEqual(-3000000000000000, board.evaluate_window(window, player))
        player = 2
        window = [1, 1, 1, 0]
        self.assertEqual(-3000000000000000, board.evaluate_window(window, player))

    def test_score_position(self):
        board = Board(self._height, self._width)
        board.move_on_board(1, 1)
        board.move_on_board(1, 1)
        board.move_on_board(1, 1)
        board.move_on_board(2, 1)
        score = board.score_position(1)
        self.assertEqual(330, score)

        score = board.score_position(2)
        self.assertEqual(-3000000000000000, score)

    def test_get_board_is_full(self):
        board = Board(self._height, self._width)
        for row in range(self._height):
            for col in range(board.width):
                if row != self._height - 1 or col != board.width - 1:
                    board.move_on_board(col, 1)
        self.assertEqual(board.get_board_is_full(), False)
        board.move_on_board(board.width - 1, 2)
        self.assertEqual(board.get_board_is_full(), True)

    def test_board_to_table(self):
        board = Board(self._height, self._width)
        table = board.board_to_table()

    def test_get_valid_moves(self):
        board = Board(self._height, self._width)
        valid_moves = board.get_valid_moves()
        self.assertListEqual(valid_moves, [0, 1, 2, 3, 4, 5, 6])
        for row in range(self._height):
            for col in range(board.width):
                if row != self._height - 1 or col != board.width - 1:
                    board.move_on_board(col, 1)

        valid_moves = board.get_valid_moves()
        self.assertListEqual(valid_moves, [6])


class TestValidators(unittest.TestCase):
    def setUp(self):
        self._board = Board(6, 7)
        self._move_validator = MoveValidator()
        self._input_validator = InputValidator()

    def test_validate_user_input(self):
        self._input_validator.validate_user_input('1')
        self.assertRaises(InputError, self._input_validator.validate_user_input, '7')
        self.assertRaises(InputError, self._input_validator.validate_user_input, 'a1')

    def test_validate_move(self):
        self._move_validator.validate_move(1, self._board)
        for _ in range(6):
            self._board.move_on_board(1, 1)
        self.assertRaises(MoveError, self._move_validator.validate_move, 1, self._board)
