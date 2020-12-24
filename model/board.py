from texttable import  Texttable

class Position:
    def __init__(self, coord_x, coord_y):
        self._x = coord_x
        self._y = coord_y

    @property
    def x(self):
        return self._x

    def decrement_x(self):
        self._x -= 1

    @property
    def y(self):
        return self._y


class Board:
    def __init__(self, height, width):
        self._height = height
        self._width = width
        self.create_board()
        self.create_available_moves()

    def create_board(self):
        self._board = [[] for i in range(self._height)]
        for row in range(len(self._board)):
            for column in range(self._width):
                self._board[row].append(0)

    def create_available_moves(self):
        self._available_moves = []
        for column in range(0, self._width):
            self._available_moves.append(Position(self._height - 1, column))

    @property
    def width(self):
        return self._width

    def apply_move_on_board(self, row, column, value):
        self._board[row][column] = value
        self._available_moves[column].decrement_x()

    def move_on_board(self,column,value):
        position = self.get_available_move_on_column(column)
        self.apply_move_on_board(position.x,position.y,value)

    def get_certain_value(self, row, column):
        return self._board[row][column]

    def get_available_moves(self):
        return self._available_moves

    def get_valid_moves_for_ai(self):
        return [move.y for move in self._available_moves]

    def get_available_move_on_column(self, column):
        for row in range(len(self._board) - 1, -1, -1):
            if self.get_certain_value(row, column) == 0:
                return Position(row, column)
        return -1

    def get_board_is_full(self):
        for row in self._board:
            for value in row:
                if value == 0:
                    return False
        return True

    def check_horizontal_pieces(self, position, winning_number):
        row = position.x
        column = position.y
        value = self.get_certain_value(row, column)
        index = 0

        won = True
        while column + index < self._width and index < winning_number and won is True:
            if self.get_certain_value(row, column + index) != value:
                won = False
            index += 1

        if won and index > 1:
            return value

        won = True
        index = 0
        while column - index > -1 and index < winning_number and won is True:
            if self.get_certain_value(row, column - index) != value:
                won = False
            index += 1

        if won and index > 1:
            return value

        return None

    def check_vertical_pieces(self, position, winning_number):
        row = position.x
        column = position.y
        value = self.get_certain_value(row, column)
        index = 0

        won = True
        while row + index < self._height and index < winning_number and won is True:
            if self.get_certain_value(row + index, column) != value:
                won = False
            index += 1

        if won and index > 1:
            return value

        index = 0
        won = True
        while row - index > -1 and index < winning_number:
            if self.get_certain_value(row - index, column) != value and won is True:
                won = False
            index += 1

        if won and index > 1:
            return value

        return None

    def check_diagonal_pieces(self, position, winning_number):
        row = position.x
        column = position.y
        value = self.get_certain_value(row, column)
        index = 0

        won = True
        while row - index > -1 and column - index > -1 and index < winning_number and won is True:
            if self.get_certain_value(row - index, column - index) != value:
                won = False
            index += 1

        if won and index > 1:
            return value

        index = 0
        won = True
        while row - index > -1 and column + index < self._width and index < winning_number and won is True:
            if self.get_certain_value(row - index, column + index) != value:
                won = False
            index += 1

        if won and index > 1:
            return value

        index = 0
        won = True
        while row + index < self._height and column - index > -1 and index < winning_number and won is True:
            if self.get_certain_value(row + index, column - index) != value:
                won = False
            index += 1

        if won and index > 1:
            return value

        index = 0
        won = True
        while row + index < self._height and column + index < self._width and index < winning_number and won is True:
            if self.get_certain_value(row + index, column + index) != value:
                won = False
            index += 1

        if won and index > 1:
            return value

        return None

    def game_won(self,position):
        winner = self.check_horizontal_pieces(position, 4)
        if winner != None:
            return winner
        winner = self.check_vertical_pieces(position, 4)
        if winner != None:
            return winner
        winner = self.check_diagonal_pieces(position, 4)
        if winner != None:
            return winner
        return None

    def board_to_table(self):
        table = Texttable()
        for row in range(0,self._height):
            board_row = []
            table.add_row(self._board[row])
        return table

    def count_sequence(self,player,length):
        pass

    def vertical_sequence(self,position,length):
        pass

    def horizontal_sequence(self,position,length):
        pass


    def evaluate_state_of_board(self):
        pass


