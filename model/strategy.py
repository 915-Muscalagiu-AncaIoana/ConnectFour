from random import shuffle
import copy


class StrategyAI:
    def minimax_alpha_beta_algorithm(self, board, depth, player):
        valid_moves = board.get_valid_moves_for_ai()
        shuffle(valid_moves)
        best_move = valid_moves[0]
        best_score = float("-inf")

        alpha = float("-inf")
        beta = float("-inf")

        if player == 2:
            opponent = 1
        else:
            opponent = 2

        for move in valid_moves:
            ai_board = copy.deepcopy(board)
            ai_board.move_on_board(move, player)
            board_score = self.minimize_beta(ai_board, depth - 1, alpha, beta, player, opponent)
            if board_score > best_score:
                best_score = board_score
                best_move = move

        return best_move

    def minimize_beta(self, board, depth, a, b, player, opponent):
        valid_moves = []
        for column in range(board.width):
            position = board.get_available_move_on_column(column)
            if position != -1:
                board.apply_move_on_board(column)
                valid_moves.append(column)

        #todo UTILITY VALUE
        if depth == 0 or len(valid_moves) == 0 or board.game_won() is not None:
            return

        valid_moves = board.get_valid_moves_for_ai()
        beta = b

        for move in valid_moves:
            board_score = float("inf")
            if a < beta:
                ai_board = copy.deepcopy(board)
                ai_board.move_on_board(move, opponent)
                board_score = self.maximize_alpha(ai_board, depth - 1, a, beta, player, opponent)

            if board_score < beta:
                beta = board_score
        return beta

    def maximize_alpha(self, board, depth, a, b, player, opponent):
        valid_moves = []
        for column in range(board.width):
            position = board.get_available_move_on_column(column)
            if position != -1:
                board.apply_move_on_board(column)
                valid_moves.append(column)

        # todo UTILITY VALUE
        if depth == 0 or len(valid_moves) == 0 or board.game_won() is not None:
            return

        alpha = a

        for move in valid_moves:
            board_score = float("-inf")
            if alpha < a:
                ai_board = copy.deepcopy(board)
                ai_board.move_on_board(move, opponent)
                board_score = self.maximize_alpha(ai_board, depth - 1, alpha, b, player, opponent)

            if board_score > alpha:
                alpha = board_score
        return alpha


