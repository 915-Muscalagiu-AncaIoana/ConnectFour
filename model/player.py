class Player:
    """
    Player - Base class for entities Computer and Human
    value - the value associated with each player
            1 - the human
            2 - the computer
    """

    def __init__(self, value):
        self._value = value

    def player_move(self, board, row, column):
        """
          This function makes a move of a player on the board by marking the cell in the matrix of the
        board with the player's specific value
        :param board: the board the player makes a move on
        :param row: the row of the board where the move will be made
        :param column: the column of the board where the move will be made
        """
        board.apply_move_on_board(row, column, self._value)


class Human(Player):
    """
    Human - A class derived from the entity player, represents the entity Human in the Game
    """

    def __init__(self, value):
        super().__init__(value)

    def human_move(self, board, row, column):
        """
            This function makes a move given by the human on the board by marking the cell in the matrix of the
        board with the human's specific value (1)
        :param board: the board the human makes a move on
        :param row: the row of the board where the move will be made
        :param column: the column of the board where the move will be made
        """
        super().player_move(board, row, column)


class Computer(Player):
    """
    Computer - A class derived from the entity player, represents the entity Computer in the Game
    The Computer has one more attribute comparing to the general player: its strategy of playing the game
    """

    def __init__(self, value, strategy):
        super().__init__(value)
        self._strategy = strategy

    def computer_move(self, board):
        """
            This function makes a move for the computer on the board by marking the cell in the matrix of the
        board with the computer's specific value (2)
            The move made for the computer is chosen depending on its strategy to find the best possible move
        :param board: the board the computer makes a move on
        """
        computer = self._value
        args = (board, 4, float("-inf"), float("inf"), True, computer)
        best_move = self._strategy.minimax(*args)[0]
        board.move_on_board(best_move, computer)
