#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Display class of McGyver Maze"""

import pygame
import constants
from position import Position
import sys


class Display:

    """class contains
    method for show the maze on the screen
    method for catch the items in the maze
    """

    def __init__(self, labyrinth):
        """initializing labyrinth instance"""

        self.labyrinth = labyrinth

    def init_display(self):
        """initializing pygame variables"""

        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(constants.WINDOW_TITLE)
        icon = pygame.image.load(constants.MCGYVER)
        pygame.display.set_icon(icon)
        self.window = pygame.display.set_mode(
            (constants.HEIGHT, constants.WIDTH))
        self.black_bg = pygame.Surface((constants.HEIGHT, constants.WIDTH))
        self.black_bg.fill((constants.BG_COLOR))
        self.background = pygame.image.load(constants.BACKGROUND)
        self.wall = pygame.image.load(constants.WALL)
        self.mcgyver = pygame.image.load(constants.MCGYVER).convert_alpha()
        self.guardian = pygame.image.load(constants.GUARDIAN).convert_alpha()
        self.end = pygame.image.load(constants.END).convert_alpha()
        self.ether = pygame.image.load(constants.ETHER).convert_alpha()
        self.tube = pygame.image.load(constants.TUBE).convert_alpha()
        self.needle = pygame.image.load(constants.NEEDLE).convert_alpha()

    def update_display(self):
        """Method refresh display for the maze and inventory"""

        self.window.blit(self.black_bg, (constants.BG_COLOR_POSITION))
        self.window.blit(self.background, (constants.BG_POSITION))

    def show_display(self):
        """Method showing the maze at the screen and all character and items"""

        for y in range(self.labyrinth.height):
            for x in range(self.labyrinth.width):
                position = Position(x, y)
                if position in self.labyrinth.wall:
                    self.window.blit(
                        self.wall,
                        (x * constants.SPR_SIZE,
                         y * constants.SPR_SIZE))
                elif position == self.labyrinth.hero:
                    self.window.blit(
                        self.mcgyver,
                        (x * constants.SPR_SIZE,
                         y * constants.SPR_SIZE))
                elif position == self.labyrinth.guardian:
                    self.window.blit(
                        self.guardian,
                        (x * constants.SPR_SIZE,
                         y * constants.SPR_SIZE))
                elif position == self.labyrinth.end:
                    self.window.blit(
                        self.end,
                        (x * constants.SPR_SIZE,
                         y * constants.SPR_SIZE))
                elif position in self.labyrinth.ether:
                    self.window.blit(
                        self.ether,
                        (x * constants.SPR_SIZE,
                         y * constants.SPR_SIZE))
                elif position in self.labyrinth.needle:
                    self.window.blit(
                        self.needle,
                        (x * constants.SPR_SIZE,
                         y * constants.SPR_SIZE))
                elif position in self.labyrinth.tube:
                    self.window.blit(
                        self.tube,
                        (x * constants.SPR_SIZE,
                         y * constants.SPR_SIZE))

    def catch_items_gui(self):
        """Method that allows MacGyver to take the objects in the maze
        and check the inventory when the position of McGyver is on
        Guardian position.
        """

        font = pygame.font.SysFont(
            constants.FONT_POLICE,
            constants.FONT_SIZE,
            constants.FONT_BOLD)
        self.result = len(self.labyrinth.inventory)
        self.text = font.render("items: " +
                                str(self.result), 1, (constants.FONT_COLOR))
        self.window.blit(self.text, (constants.FONT_POSITION))

        if self.labyrinth.hero in self.labyrinth.ether:
            self.labyrinth.inventory.append(self.labyrinth.ether)
            self.window.blit(self.ether, (constants.POSITION_ITEMS.pop(0)))
            self.labyrinth.ether = []

        elif self.labyrinth.hero in self.labyrinth.tube:
            self.labyrinth.inventory.append(self.labyrinth.tube)
            self.window.blit(self.tube, (constants.POSITION_ITEMS.pop(0)))
            self.labyrinth.tube = []

        elif self.labyrinth.hero in self.labyrinth.needle:
            self.labyrinth.inventory.append(self.labyrinth.needle)
            self.window.blit(self.needle, (constants.POSITION_ITEMS.pop(0)))
            self.labyrinth.needle = []

        elif self.labyrinth.hero == self.labyrinth.guardian:

            if self.result == constants.RESULT:
                self.win = font.render(
                    (constants.WIN), 1, (constants.FONT_COLOR))
                self.window.blit(self.win, (constants.FONT_RESULT_POSITION))
                self.win
                self.labyrinth.free.append(self.labyrinth.end)

            else:
                self.loose = font.render(
                    (constants.LOOSE), 1, (constants.FONT_COLOR))
                self.window.blit(self.loose, (constants.FONT_RESULT_POSITION))
                self.loose
                sys.exit()
