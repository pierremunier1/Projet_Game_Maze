#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Items class of McGyver maze"""

from position import Position
from random import sample
import constants


class Items:

    """class items contains all method to generate positions"""

    def __init__(self, labyrinth):
        """initializing labyrinth instance"""

        self.labyrinth = labyrinth
        self.labyrinth.items = self.random()

    def random(self):
        """method check random position items into the maze"""

        return sample(self.labyrinth.free, constants.RANDOMS_ITEMS)

    def add_random_position(self):
        """method add ramdom position for every items"""

        self.labyrinth.ether.append(self.labyrinth.items[0])
        self.labyrinth.tube.append(self.labyrinth.items[1])
        self.labyrinth.needle.append(self.labyrinth.items[2])
