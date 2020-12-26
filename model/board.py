from texttable import Texttable


class Position:
    """

    """
    def __init__(self, coord_x, coord_y):
        self._x = coord_x
        self._y = coord_y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class Board:
    """
        This is the class for the entity Board, which has a specific size ( a height and a width)
    """
    def __init__(self, height, width):
        self._height = height
        self._width = width
        self.create_board()
        # self.create_available_moves()

    def create_board(self):
        """
            This function creates the board ( when creating a new object of this type),
        which has a format of multiple lists within a list and with all positions intialized with 0 (signifying an empty cell)
        """
        self._board = [[] for i in range(self._height)]
        for row in range(len(self._board)):
            for column in range(self._width):
                self._board[row].append(0)

    # def create_available_moves(self):
    #     self._available_moves = []
    #     for column in range(0, self._width):
    #         self._available_moves.append(Position(self._height - 1, column))

    @property
    def width(self):
        return self._width

    def apply_move_on_board(self, row, column, value):
        """
            This function applies a move on the board by assigning the cell of the matrix
        the value of the player which made the move
        :param row: the row of the board where the move will be made
        :param column: the column of the board where the move will be made
        :param value: the value of the player that makes the move
        """
        self._board[row][column] = value
        # self._available_moves[column].decrement_x()

    def move_on_board(self, column, value):
        """
            This function searches for the row available on a certain column and places a piece on that position
        :param column: the column of the board where the move will be made
        :param value: the value of the player that makes the move
        """
        position = self.get_available_move_on_column(column)
        self.apply_move_on_board(position.x, position.y, value)

    def get_certain_value(self, row, column):
        """
            This function returns the value of a certain cell in the matrix of the board
        :param row: the row of the cell required
        :param column: the column of the cell required
        """
        return self._board[row][column]

    # def get_available_moves(self):
    #     return self._available_moves

    # def get_valid_moves_for_ai(self):
    #     return [move.y for move in self._available_moves if move.y >= 0]

    def get_valid_moves(self):
        """
            This function searches for the column that there can still be dropped pieces on (which still contain a valid move)
        :return: the list of valid moves on the board ( the columns that still have at least one empty row)
        """
        valid_moves = []
        for col in range(self._width):
            position = self.get_available_move_on_column(col)
            if position != -1:
                valid_moves.append(col)
        return valid_moves

    def get_available_move_on_column(self, column):
        """
            This function searches for the row available on a certain column, if it exists it returns the position,
        otherwise it returns -1
        :param column: the column of the board
        :return: the position of the available move or -1 if there is no valid move on this column
        """
        for row in range(len(self._board) - 1, -1, -1):
            if self.get_certain_value(row, column) == 0:
                return Position(row, column)
        return -1

    def get_board_is_full(self):
        """
            This function checks if the board is full (has only values of 1 and 2). If the board is full it means
        that the game was not won yet therefore meaning that the game is a draw
        :return: True - the board is full
                 False - otherwise
        """
        for row in self._board:
            for value in row:
                if value == 0:
                    return False
        return True

    # def check_vertical_pieces(self, position, length):
    #     row = position.x
    #     column = position.y
    #     value = self.get_certain_value(row, column)
    #     count = 0
    #
    #     for row_index in range(row, self._height):
    #         if self._board[row_index][column] == value:
    #             count += 1
    #         else:
    #             break
    #
    #     if count >= length:
    #         return 1
    #     else:
    #         return 0
    #
    # def check_horizontal_pieces(self, position, length):
    #     row = position.x
    #     column = position.y
    #     value = self.get_certain_value(row, column)
    #     count = 0
    #
    #     for col_index in range(column, self._width):
    #         if self._board[row][col_index] == value:
    #             count += 1
    #         else:
    #             break
    #
    #     if count >= length:
    #         return 1
    #     else:
    #         return 0
    #
    # def check_positive_diagonal_pieces(self, position, length):
    #     row = position.x
    #     column = position.y
    #     value = self.get_certain_value(row, column)
    #     count = 0
    #     col_index = column
    #     for row_index in range(row, self._height):
    #         if col_index >= self._width:
    #             break
    #         elif self._board[row_index][col_index] == value:
    #             count += 1
    #         else:
    #             break
    #         col_index += 1
    #     if count >= length:
    #         return 1
    #     else:
    #         return 0
    #
    # def check_negative_diagonal_pieces(self, position, length):
    #     row = position.x
    #     column = position.y
    #     value = self.get_certain_value(row, column)
    #     count = 0
    #     col_index = column
    #     for row_index in range(row, -1, -1):
    #         if col_index >= self._width:
    #             break
    #         elif self._board[row_index][col_index] == value:
    #             count += 1
    #         else:
    #             break
    #         col_index += 1
    #     if count >= length:
    #         return 1
    #     else:
    #         return 0

    def game_won(self):
        """
            This function checks if the game was won and returns the winner if so
        :return: human - the winner is the human playing with value 1
                 computer - the winner is the computer playing with value 1
                 None - the game wasn't won yet
        """
        computer = 2
        human = 1
        if self.winning_move(human):
            return human
        elif self.winning_move(computer):
            return computer
        else:
            return None

    def winning_move(self, player):
        """
            This function checks if a player has won by verifying all the possible combinations of 4 pieces within the table
        to see if the player's value appears 4 times consecutively
        :param player: the value the player plays with on the table
        :return True - if the player has won
                None - otherwise
        """
        for column in range(self._width-3):
            for row in range(self._height):
                if self._board[row][column] == player and self._board[row][column+1] == player and self._board[row][
                    column+2] == player and self._board[row][column+3] == player:
                    return True

        for column in range(self._width):
            for row in range(self._height-3):
                if self._board[row][column] == player and self._board[row+1][column] == player and self._board[row+2][
                    column] == player and self._board[row+3][column] == player:
                    return True

        for column in range(self._width-3):
            for row in range(self._height-3):
                if self._board[row+1][column+1] == player and self._board[row+2][column+2] == player and self._board[row+3][
                    column+3] == player and self._board[row][column] == player:
                    return True

        for column in range(self._width-3):
            for row in range(3,self._height):
                if self._board[row][column] == player and self._board[row-1][column+1] == player and self._board[row-2][
                    column+2] == player and self._board[row-3][column+3] == player:
                    return True

    def evaluate_window(self, window,player):
        """
            This function checks a window (an array) of 4 cells in the board to count
        the number of pieces of a certain player are in that window. Afterwards it computes the score of the player
        by the number of the pieces he has in that window.
        - 4 pieces -> the player has won -> +100
        - 3 pieces + empty cell -> the player is close to winning -> + 5
        - 2 pieces + empty cell -> the player has a slight chance to win in the next rounds -> +2
            The function checks to see if the opponent has 3 pieces of its own in that window, meaning
        that the player must place a piece in the remaining cell to prevent the opponent from winning
        :param window: an array of 4 cells in the board
        :param player: the value assigned to the player
        :return: score - the score of the player given by this window in the board
        """
        score = 0
        if player == 1:
            opponent = 2
        else :
            opponent = 1

        if window.count(player) == 4:
            score+= 1000
        elif window.count(player) == 3 and window.count(0) == 1 :
            score+= 5
        elif window.count(player) == 2 and window.count(0) == 2 :
            score+= 2

        if window.count(opponent) == 3 and window.count(0) == 1:
            score -=40000000

        return score

    def score_position(self,player):
        """
            This function calculates the score of a player at a certain moment in the game, by evaluating every possible
        window of 4 vertical/horizontal/diagonal adjacent cells
        :param player: the player whose score is about to be computed
        :return: score - the total score of the player at a certain moment in the game
        """
        score = 0
        center_array = [self._board[i][self._width//2] for i in range(self._height)]
        center_count = center_array.count(player)

        for row in range(self._height):
            row_array = self._board[row]
            for column in range(self._width-3):
                window = row_array[column:column+4]
                score+=self.evaluate_window(window,player)

        for column in range(self._width):
            column_array = [self._board[i][column] for i in range(self._height)]
            for row in range(self._height-3) :
                window = column_array[row:row+4]
                score += self.evaluate_window(window, player)

        for row in range(self._height - 3):
            for column in range(self._width - 3):
                window = [self._board[row+i][column+i] for i in range(4)]
                score += self.evaluate_window(window, player)

        for row in range(self._height - 3):
            for column in range(self._width - 3):
                window = [self._board[row+3-i][column+i] for i in range(4)]
                score += self.evaluate_window(window, player)
        return score

    def board_to_table(self):
        """
            This function returns the current board in a texttable format to be printed by the ui
        :return: the board as a texttable
        """
        table = Texttable()
        for row in range(0, self._height):
            board_row = []
            table.add_row(self._board[row])
        return table

    # def count_sequence(self, player, length):
    #     total_count = 0
    #
    #     for row in range(self._height):
    #         for column in range(self._width):
    #             if self._board[row][column] == player:
    #                 position = Position(row, column)
    #                 total_count += self.check_vertical_pieces(position, length)
    #                 total_count += self.check_horizontal_pieces(position, length)
    #                 total_count += (self.check_positive_diagonal_pieces(position,
    #                                                                     length) + self.check_negative_diagonal_pieces(
    #                     position, length))
    #     return total_count

    # def evaluate_state_of_board(self, player):
    #     if player == 1:
    #         opponent = 2
    #     else:
    #         opponent = 1
    #     player_fours = self.count_sequence(player, 4)
    #     player_threes = self.count_sequence(player, 3)
    #     player_twos = self.count_sequence(player, 2)
    #     player_score = player_fours * 99999 + player_threes * 999 + player_twos * 99
    #
    #     opponent_fours = self.count_sequence(opponent, 4)
    #     opponent_threes = self.count_sequence(opponent, 3)
    #     opponent_twos = self.count_sequence(opponent, 2)
    #     opponent_score = opponent_fours * 99999 + opponent_threes * 999 + opponent_twos * 99
    #
    #     if opponent_fours > 0:
    #         return float('-inf')
    #     else:
    #         return player_score - opponent_score
