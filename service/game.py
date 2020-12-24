class Game:
    def __init__(self, board, computer, human, validator):
        self._board = board
        self._computer = computer
        self._human = human
        self._game_state = False
        self._winner = None
        self._validator = validator

    def check_game_over(self, position):
        self._winner = self.check_game_won(position)
        self.check_game_draw()
        if self._game_state == True:
            return True
        return False

    def check_game_won(self, position):
        winner = self._board.game_won(position)
        if winner != None:
            self._game_state = True
        return winner

    def check_game_draw(self):
        if self._board.get_board_is_full():
            self._game_state = True

    def computer_move(self):
        position = None
        self._computer.computer_move(self._board)
        self.check_game_over(position)

    def human_move(self, column):
        self._validator.validate_move(column, self._board)
        position = self._board.get_available_move_on_column(column)
        self._human.human_move(self._board, position.x, position.y)
        self.check_game_over(position)

    def get_cell_of_board(self,row,column):
        return self._board.get_certain_value(row,column)

    def get_board(self):
        return self._board.board_to_table()

    def get_winner(self):
        return self._winner
