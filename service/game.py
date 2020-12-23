class Game:
    def __init__(self, board, strategy,validator):
        self._board = board
        self._strategy = strategy
        self._game_state = False
        self._winner = None
        self._validator = validator

    def check_game_over(self,position):
        winner = self.check_game_won(position)
        self.check_game_draw()
        if self._game_state == True:
            return True
        return False

    def check_game_won(self,position):
        winner = self._board.check_horizontal_pieces(position)
        if winner != None:
            self._game_state = True
            return winner
        winner = self._board.check_vertical_pieces(position)
        if winner != None:
            self._game_state = True
            return winner
        winner = self._board.check_diagonal_pieces(position)
        if winner != None:
            self._game_state = True
            return winner

    def check_game_draw(self):
        if self._board.get_board_is_full() == True:
            self._game_state = True

    def computer_move(self):
        position = None
        self.check_game_over(position)

    def human_move(self, column):
        self._validator.validate_human_move(column,self._board)
        position = self._board.get_available_move_on_column(column)
        self._board.apply_move_on_board(position.x,position.y,1)
        self.check_game_over(position)

    def get_board(self):
        return self._board

    def get_winner(self):
        return self._winner