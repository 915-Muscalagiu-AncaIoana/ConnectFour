class Player:
    def __init__(self, value):
        self._value = value

    def player_move(self, board, row, column):
        board.apply_move_on_board(row, column, self._value)


class Human(Player):
    def __init__(self, value):
        super().__init__(value)

    def human_move(self, board, row, column):
        super().player_move(board, row, column)


class Computer(Player):
    def __init__(self, value, strategy):
        super().__init__(value)
        self._strategy = strategy

    def computer_move(self, board):
        computer = 2
        best_move = self._strategy.minimax_alpha_beta_algorithm(board, 4, computer)
        board.move_on_board( best_move, computer)
