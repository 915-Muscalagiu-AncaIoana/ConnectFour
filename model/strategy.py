import random
import copy


class StrategyAI:
    """
       This class represents the Strategy used by the Computer(the AI) to play the Game
    (using the minmax algorithm for finding the best move)
    """

    def minimax(self, board, depth, alpha, beta, maximizing_player, player):
        """

        :param board: the board on which the minimax algorithm tries to find the best possible move
        :param depth: the depth of the tree
        :param alpha:
        :param beta:
        :param maximizing_player:
        :param player:
        :return:
        """
        valid_moves = board.get_valid_moves()
        is_terminal = self.is_terminal_node(board)
        if depth == 0 or is_terminal:
            if is_terminal:
                if board.game_won() == player:
                    return (None, 10000000)
                elif board.game_won() == player - 1:
                    return (None, -10000000)
                else:
                    return (None, 0)
            else:
                return (None, board.score_position(player))

        if depth == 2 and board.game_won() == player:
            return (None, float("inf"))

        if maximizing_player:
            value = float('-inf')
            column = random.choice(valid_moves)
            for col in valid_moves:
                ai_board = copy.deepcopy(board)
                ai_board.move_on_board(col, player)
                new_score = self.minimax(ai_board, depth - 1, alpha, beta, False, player)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break

            return column, value

        else:
            value = float('inf')
            column = random.choice(valid_moves)
            for col in valid_moves:
                ai_board = copy.deepcopy(board)
                ai_board.move_on_board(col, player - 1)
                new_score = self.minimax(ai_board, depth - 1, alpha, beta, True, player)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break

            return column, value

    def is_terminal_node(self, board):
        """

        :param board:
        :return:
        """
        return board.winning_move(1) or board.winning_move(2) or len(board.get_valid_moves()) == 0

    # def minimax_alpha_beta_algorithm(self, board, depth, player):
    #     valid_moves = board.get_valid_moves_for_ai()
    #     #shuffle(valid_moves)
    #     best_move = valid_moves[0]
    #     best_score = float("-inf")
    #
    #     alpha = float("-inf")
    #     beta = float("inf")
    #
    #     if player == 2:
    #         opponent = 1
    #     else:
    #         opponent = 2
    #
    #     for move in valid_moves:
    #         ai_board = copy.deepcopy(board)
    #         ai_board.move_on_board(move, player)
    #         board_score = self.minimize_beta(ai_board, depth - 1, alpha, beta, player, opponent)
    #         if board_score > best_score:
    #             best_score = board_score
    #             best_move = move
    #
    #     return best_move
    #
    # def minimize_beta(self, board, depth, a, b, player, opponent):
    #     valid_moves = []
    #     for column in range(board.width):
    #         position = board.get_available_move_on_column(column)
    #         if position != -1:
    #             new_board = copy.deepcopy(board)
    #             new_board.apply_move_on_board(position.x, position.y, opponent)
    #             valid_moves.append(column)
    #
    #     if depth == 0 or len(valid_moves) == 0 or board.game_won() is not None:
    #         return board.evaluate_state_of_board(player)
    #
    #     valid_moves = board.get_valid_moves_for_ai()
    #     beta = b
    #
    #     for move in valid_moves:
    #         board_score = float("inf")
    #         if a < beta:
    #             ai_board = copy.deepcopy(board)
    #             ai_board.move_on_board(move, player)
    #             board_score = self.maximize_alpha(ai_board, depth - 1, a, beta, player, opponent)
    #
    #         if board_score < beta:
    #             beta = board_score
    #     return beta
    #
    # def maximize_alpha(self, board, depth, a, b, player, opponent):
    #     valid_moves = []
    #     for column in range(board.width):
    #         position = board.get_available_move_on_column(column)
    #         if position != -1:
    #             new_board = copy.deepcopy(board)
    #             new_board.apply_move_on_board(position.x, position.y, player)
    #             valid_moves.append(column)
    #
    #     if depth == 0 or len(valid_moves) == 0 or board.game_won() is not None:
    #         return board.evaluate_state_of_board(player)
    #
    #     alpha = a
    #
    #     for move in valid_moves:
    #         board_score = float("-inf")
    #         if alpha < a:
    #             ai_board = copy.deepcopy(board)
    #             ai_board.move_on_board(move, opponent)
    #             board_score = self.minimize_beta(ai_board, depth - 1, alpha, b, player, opponent)
    #
    #         if board_score > alpha:
    #             alpha = board_score
    #     return alpha
