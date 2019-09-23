#!/usr/bin/python
# -*- coding: utf-8 -*-
from labyrinth import Maze
from position import Position
from random import sample
from hero import Hero
from items import Items


class Game:

    def __init__(self):
        # initializing all class instances from another python files"""

        self.labyrinth = Maze()
        self.labyrinth.build('laby.txt')
        self.hero = Hero(self.labyrinth)
        self.items = Items(self.labyrinth)

    def choice(self):
        # user ability to choice direction into the maze with directionnaly key

        direction = input('***choose direction : ')
        select = ("up", "down", "left", "right")
        if direction in select:
            self.hero.move(direction)


def main():

    game = Game()
    game.items.add_random_position()

    while True:

        game.labyrinth.show()
        game.choice()
        game.hero.catch_items()
        game.hero.result_inventory()


if __name__ == "__main__":
    main()
