#!/usr/bin/python
# -*- coding: utf-8 -*-
from position import Position
from random import sample
import constants


class Items:

    """Class of the Items"""

    def __init__(self, labyrinth):

        self.labyrinth = labyrinth
        self.labyrinth.items = self.random()

    def random(self):
        # Method check random position items into the maze

        return sample(self.labyrinth.free, constants.RANDOMS_ITEMS)

    def add_random_position(self):
        # Method add ramdom position for every items"""

        self.labyrinth.ether.append(self.labyrinth.items[0])
        self.labyrinth.tube.append(self.labyrinth.items[1])
        self.labyrinth.needle.append(self.labyrinth.items[2])
