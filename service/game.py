class Game:
    """
        This is the class that handles all the processes in the Game : the moves of both players
    and the state of the game (if it is won/ draw/ not finished yet)
    """
    def __init__(self, board, computer, human, validator):
        self._board = board
        self._computer = computer
        self._human = human
        self._game_state = False
        self._winner = None
        self._validator = validator

    def check_game_over(self):
        """

        :return:
        """
        self._winner = self.check_game_won()
        self.check_game_draw()
        if self._game_state == True:
            return True
        return False

    def check_game_won(self):
        """

        :return:
        """
        winner = self._board.game_won()
        if winner is not None:
            self._game_state = True
        return winner

    def check_game_draw(self):
        """

        :return:
        """
        if self._board.get_board_is_full():
            self._game_state = True

    def computer_move(self):
        """

        :return:
        """
        self._computer.computer_move(self._board)
        self.check_game_over()

    def human_move(self, column):
        """

        :param column:
        :return:
        """
        self._validator.validate_move(column, self._board)
        position = self._board.get_available_move_on_column(column)
        self._human.human_move(self._board, position.x, position.y)
        self.check_game_over()

    def get_cell_of_board(self,row,column):
        """

        :param row:
        :param column:
        :return:
        """
        return self._board.get_certain_value(row,column)

    def get_board(self):
        """
            This function returns the board of the game in a texttable format in order to be printed in the ui
        :return: board
        """
        return self._board.board_to_table()

    def get_winner(self):
        """
            This function returns the winner of the game ( the Computer / the Human / None - draw/game not finished yet)
        :return: winner -> the current winner of the game

        """
        return self._winner
