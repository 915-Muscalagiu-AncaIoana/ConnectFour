from model.validators import InputError, MoveError


class Ui:
    def __init__(self, game, validator):
        self._game = game
        self._validator = validator

    def start(self):
        turn = 0
        while self._game.check_game_over() == False:
            try:
                if turn == 0:
                    self.ui_print_board()
                    print('Please choose the column you want to place the piece on: ')
                    column = input()
                    self._validator.validate_user_input(column)
                    column = int(column)
                    self._game.human_move(column)
                    turn = 1
                else:
                    self._game.computer_move()
                    turn = 0
            except InputError as ie:
                print(str(ie))
            except MoveError as me:
                print(str(me))
        if self._game.get_winner() == 1 :
            print('YOU WON!')
        elif self._game.get_winner() == 2 :
            print('YOU LOST!')
        else:
            print('THE GAME IS DRAW!')

    def ui_print_board(self):
        print(str(self._game.get_board()))
