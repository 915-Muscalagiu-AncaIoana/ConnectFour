class InputError(Exception):
    pass

class MoveError(Exception):
    pass

class InputValidator:
    @staticmethod
    def validate_user_input(column):
        """
          This function is used to validate the user's input (the column that he wants to drop a piece on)
        :param column: the input given by the user as a column
        :raises InputError - if the column is not an integer value between 0 and 6
        """
        if not column.isdigit():
           raise InputError('The column you place a piece on must be an integer value between 0 and 6')
        column = int(column)
        if column < 0 or column > 6 :
            raise InputError('The column you place a piece on must be an integer value between 0 and 6')

class MoveValidator:
    @staticmethod
    def validate_move(column,board):
        """
          This function is used to validate a move, to verify if it doesn't exceed the limits of the board
        :param column: the column on which the move is about to be made
        :param board: the board the move is about to be made on
        :raises MoveError if the column is full of pieces, meaning that the move is not possible
        """
        if board.get_available_move_on_column(column).x < 0 :
            raise MoveError('This move is not possible because the column is full of pieces')