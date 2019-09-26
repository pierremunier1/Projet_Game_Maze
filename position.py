#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Position class of McGyver maze"""


class Position:

    """class which manages the elements' position in the labyrinth"""

    def __init__(self, x, y):
        """initializing x and y"""

        self.x = x
        self.y = y

    def up(self):
        """method permit to move up McGyver"""

        return Position(self.x, self.y - 1)

    def down(self):
        """method permit to move down McGyver"""

        return Position(self.x, self.y + 1)

    def left(self):
        """method permit to move left McGyver"""

        return Position(self.x - 1, self.y)

    def right(self):
        """method permit to move right McGyver"""

        return Position(self.x + 1, self.y)

    def __eq__(self, other):
        """method permit to verify position"""

        return (self.x, self.y) == (other.x, other.y)
