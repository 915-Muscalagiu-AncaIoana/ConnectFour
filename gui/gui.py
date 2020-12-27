import pygame
import sys
import math
from model.validators import MoveError


class GUI:
    def __init__(self, square_size, column_count, row_count, game, validator):
        self._column_count = column_count
        self._row_count = row_count
        self._square_size = square_size
        width = column_count * square_size
        height = (row_count + 1) * square_size
        self._size = (width, height)
        self._background_color = (0, 0, 255)
        self._empty_colour = (0, 0, 0)
        self._computer_colour = (255, 185, 15)
        self._human_colour = (220, 20, 60)
        self._game = game
        self._validator = validator

    def draw_board(self):
        for column in range(self._column_count):
            for row in range(self._row_count):
                pygame.draw.rect(self._screen, self._background_color, (
                    column * self._square_size, (row + 1) * self._square_size, self._square_size, self._square_size))
                if self._game.get_cell_of_board(row, column) == 0:
                    pygame.draw.circle(self._screen, self._empty_colour,
                                       ((column + 0.5) * self._square_size, (row + 1 + 0.5) * self._square_size),
                                       self._square_size // 2 - 5)
                elif self._game.get_cell_of_board(row, column) == 1:
                    pygame.draw.circle(self._screen, self._human_colour,
                                       ((column + 0.5) * self._square_size, (row + 1 + 0.5) * self._square_size),
                                       self._square_size // 2 - 5)
                elif self._game.get_cell_of_board(row, column) == 2:
                    pygame.draw.circle(self._screen, self._computer_colour,
                                       ((column + 0.5) * self._square_size, (row + 1 + 0.5) * self._square_size),
                                       self._square_size // 2 - 5)

    def start(self):
        pygame.init()
        self._screen = pygame.display.set_mode(self._size)
        self._font = pygame.font.SysFont("monospace", 75)
        turn = 0
        while self._game.get_winner() == None:
            try:
                for event in pygame.event.get() :
                    self.draw_board()
                    pygame.display.update()
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEMOTION:
                        pygame.draw.rect(self._screen, self._empty_colour,
                                         (0, 0, self._column_count * self._square_size, self._square_size))
                        position = event.pos[0]
                        if turn == 0:
                            pygame.draw.circle(self._screen, self._human_colour, (position, int(self._square_size / 2)),
                                               self._square_size // 2 - 5)
                        else:
                            pygame.draw.circle(self._screen, self._computer_colour,
                                               (position, int(self._square_size / 2)),
                                               self._square_size // 2 - 5)
                        pygame.display.update()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(self._screen, self._empty_colour,
                                         (0, 0, self._column_count * self._square_size, self._square_size))
                        if turn == 0:
                            column = int(math.floor(event.pos[0] / self._square_size))
                            self._game.human_move(column)
                            if self._game.check_game_over() == True:
                                break
                            turn = 1
                if turn == 1:
                    pygame.time.wait(500)
                    self._game.computer_move()
                    if self._game.check_game_over() == True:
                        break
                    turn = 0
            except MoveError as me:
                continue

        self.draw_board()
        pygame.display.update()

        if self._game.get_winner() == 1:
            label = self._font.render('YOU WON!', True, self._human_colour)
            self._screen.blit(label,(60,10))
        elif self._game.get_winner() == 2:
            label = self._font.render('YOU LOST!', True, self._computer_colour)
            self._screen.blit(label, (40, 10))
        else:
            label = self._font.render('THE GAME IS DRAW!', True, self._human_colour)
            self._screen.blit(label, (40, 10))
        pygame.display.update()
        pygame.time.wait(3000)
