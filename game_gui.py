#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Game class of McGyver maze"""

from labyrinth import Maze
from position import Position
from random import sample
from hero import Hero
from items import Items
from display_gui import Display
import constants
import pygame
import sys


class Game:

    """class contains the methods necessary to launch the McGyver maze"""

    def __init__(self):
        """initializing all class of the game"""

        self.labyrinth = Maze()
        self.labyrinth.build('maze.txt')
        self.hero = Hero(self.labyrinth)
        self.items = Items(self.labyrinth)
        self.display_gui = Display(self.labyrinth)

    def choice(self):
        """choice direction into the maze with keyboard key"""

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.hero.move('right')
                elif event.key == pygame.K_LEFT:
                    self.hero.move('left')
                elif event.key == pygame.K_DOWN:
                    self.hero.move('down')
                elif event.key == pygame.K_UP:
                    self.hero.move('up')
                    self.display_gui.update_display()

            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()


def main():

    game = Game()
    game.items.add_random_position()
    game.display_gui.init_display()

    while True:

        game.choice()
        game.display_gui.update_display()
        game.display_gui.show_display()
        game.display_gui.catch_items_gui()
        pygame.display.flip()


if __name__ == '__main__':
    main()
