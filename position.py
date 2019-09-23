#!/usr/bin/python
# -*- coding: utf-8 -*-


class Position:

    """Class which manages the elements' position in the labyrinth"""

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def up(self):

        return Position(self.x, self.y - 1)

    def down(self):

        return Position(self.x, self.y + 1)

    def left(self):

        return Position(self.x - 1, self.y)

    def right(self):

        return Position(self.x + 1, self.y)

    def __str_(self):

        return str((self.x, self.y))

    def __repr__(self):

        return 'Position(x={},y={})'.format(self.x, self.y)

    def __eq__(self, other):

        return (self.x, self.y) == (other.x, other.y)
