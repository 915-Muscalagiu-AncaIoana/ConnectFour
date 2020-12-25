from texttable import Texttable


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

    def move_on_board(self, column, value):
        position = self.get_available_move_on_column(column)
        self.apply_move_on_board(position.x, position.y, value)

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

    def check_vertical_pieces(self, position, length):
        row = position.x
        column = position.y
        value = self.get_certain_value(row, column)
        count = 0

        for row_index in range(row, self._height):
            if self._board[row_index][column] == value:
                count += 1
            else:
                break

        if count >= length:
            return 1
        else:
            return 0

    def check_horizontal_pieces(self, position, length):
        row = position.x
        column = position.y
        value = self.get_certain_value(row, column)
        count = 0

        for col_index in range(column, self._width):
            if self._board[row][col_index] == value:
                count += 1
            else:
                break

        if count >= length:
            return 1
        else:
            return 0

    def check_positive_diagonal_pieces(self, position, length):
        row = position.x
        column = position.y
        value = self.get_certain_value(row, column)
        count = 0
        col_index = column
        for row_index in range(row, self._height):
            if col_index >= self._width:
                break
            elif self._board[row_index][col_index] == value:
                count += 1
            else:
                break
            col_index += 1
        if count >= length:
            return 1
        else:
            return 0

    def check_negative_diagonal_pieces(self, position, length):
        row = position.x
        column = position.y
        value = self.get_certain_value(row, column)
        count = 0
        col_index = column
        for row_index in range(row, -1, -1):
            if col_index >= self._width:
                break
            elif self._board[row_index][col_index] == value:
                count += 1
            else:
                break
            col_index += 1
        if count >= length:
            return 1
        else:
            return 0

    def game_won(self):
        computer = 2
        human = 1
        if self.count_sequence(human,4) >= 1:
            return human
        elif self.count_sequence(computer,4) >=1 :
            return computer
        else:
            return None

    def board_to_table(self):
        table = Texttable()
        for row in range(0, self._height):
            board_row = []
            table.add_row(self._board[row])
        return table

    def count_sequence(self, player, length):
        total_count = 0

        for row in range(self._height):
            for column in range(self._width):
                if self._board[row][column] == player:
                    position = Position(row, column)
                    total_count += self.check_vertical_pieces(position, length)
                    total_count += self.check_horizontal_pieces(position, length)
                    total_count += (self.check_positive_diagonal_pieces(position,
                                                                        length) + self.check_negative_diagonal_pieces(
                        position, length))
        return total_count

    def evaluate_state_of_board(self,player):
        if player == 1:
            opponent = 2
        else:
            opponent = 1
        player_fours = self.count_sequence(player,4)
        player_threes = self.count_sequence(player, 3)
        player_twos = self.count_sequence(player, 2)
        player_score = player_fours * 99999 + player_threes*999 + player_twos*99

        opponent_fours = self.count_sequence(opponent, 4)
        opponent_threes = self.count_sequence(opponent, 3)
        opponent_twos = self.count_sequence(opponent, 2)
        opponent_score = opponent_fours * 99999 + opponent_threes * 999 + opponent_twos * 99

        if opponent_fours > 0 :
            return float('-inf')
        else:
            return player_score - opponent_score


