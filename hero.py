#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Hero class of the McGyver maze"""

from position import Position
import pygame


class Hero:

    """class contains all methods for the macgyver interaction"""

    def __init__(self, labyrinth):
        """initializing labyrinth instance"""

        self.labyrinth = labyrinth
        self.labyrinth.inventory = []

    def move(self, direction):
        """check if the new position is on free space"""

        new_position = getattr(self.labyrinth.hero, direction)()
        if new_position in self.labyrinth.free:
            self.labyrinth.hero = new_position

    def catch_items(self):
        """permit at MGGyver to take every items into the maze(console mode)"""

        if self.labyrinth.hero in self.labyrinth.ether:
            self.labyrinth.inventory.append(self.labyrinth.ether)
            self.labyrinth.ether = []
        elif self.labyrinth.hero in self.labyrinth.tube:

            self.labyrinth.inventory.append(self.labyrinth.tube)
            self.labyrinth.tube = []
        elif self.labyrinth.hero in self.labyrinth.needle:

            self.labyrinth.inventory.append(self.labyrinth.needle)
            self.labyrinth.needle = []

    def result_inventory(self):
        """method to check the inventory(console mode)"""

        result = len(self.labyrinth.inventory)

        print ('Items:', result)
        if self.labyrinth.hero == self.labyrinth.guardian:
            if result == 3:
                print ("**You Win**")
            elif result != 3:
                print ("**You Loose**")
