class InputError(Exception):
    pass

class MoveError(Exception):
    pass

class InputValidator:
    @staticmethod
    def validate_user_input(column):
        if not column.isdigit():
           raise InputError('The column you place a piece on must be an integer value between 0 and 6')
        column = int(column)
        if column < 0 or column > 6 :
            raise InputError('The column you place a piece on must be an integer value between 0 and 6')

class MoveValidator:
    @staticmethod
    def validate_move(column,board):
        if board.get_available_move_on_column(column).x < 0 :
            raise MoveError('This move is not possible because the column is full of pieces')