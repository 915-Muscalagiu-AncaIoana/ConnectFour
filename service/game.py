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
            This function checks if the game is over (if it was won or if it is a draw) by searching for a winner and
        checking if the board is full
        :return: True - if the game is over
                 False - otherwise
        """
        self._winner = self.check_game_won()
        self.check_game_draw()
        if self._game_state == True:
            return True
        return False

    def check_game_won(self):
        """
            This function checks if the game is over by seeing if there is a winner , then it marks the game state as True
        and returns the winner (which is None if the game is not won yet)
        :return:
        """
        winner = self._board.game_won()
        if winner is not None:
            self._game_state = True
        return winner

    def check_game_draw(self):
        """
            This function checks if the game is a draw (if there are no more possible moves). If the board is full,
        then it marks the game state as True
        """
        if self._board.get_board_is_full():
            self._game_state = True

    def computer_move(self):
        """
            This function makes a move for the Computer computer and then checks if the game is over after the move
        """
        self._computer.computer_move(self._board)
        self.check_game_over()

    def human_move(self, column):
        """
            This function validates amd makes a move for the Human computer according to the input of the user
        and then checks if the game is over after the move
        :param column: the column that the user wants to drop a piece on
        """
        self._validator.validate_move(column, self._board)
        position = self._board.get_available_move_on_column(column)
        self._human.human_move(self._board, position.x, position.y)
        self.check_game_over()

    def get_cell_of_board(self, row, column):
        """
            This function returns the value of a cell of the board at position (row,column)
        :param row: the row of the cell
        :param column: the column of the cell
        :return: the value of the cell at position (row,column)
        """
        return self._board.get_certain_value(row, column)

    def get_board(self):
        """
            This function returns the board of the game in a texttable format in order to be printed in the ui
        :return: board.board_to_table() - the board in the texttable format
        """
        return self._board.board_to_table()

    def get_winner(self):
        """
            This function returns the winner of the game ( the Computer / the Human / None - draw/game not finished yet)
        :return: winner -> the current winner of the game

        """
        return self._winner

    def get_game_state(self):
        """
            This function returns the game state ( True - game was won or draw was reached / False - game is not finished yet)
        :return: game state -> if the game was finished or not

        """
        return self._game_state
