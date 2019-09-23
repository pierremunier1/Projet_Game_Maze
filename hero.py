#!/usr/bin/python
# -*- coding: utf-8 -*-
from position import Position
import pygame


class Hero:

    """class of the MacGyver"""

    def __init__(self, labyrinth):

        self.labyrinth = labyrinth
        self.labyrinth.inventory = []

    def move(self, direction):
        # Check if the new position is on free space

        new_position = getattr(self.labyrinth.hero, direction)()
        if new_position in self.labyrinth.free:
            self.labyrinth.hero = new_position
        else:
            pass

    def catch_items(self):
        # Permit at MGGyver to take every items into the maze

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
        # method to check the inventory

        result = len(self.labyrinth.inventory)

        print ('Items:', result)
        if self.labyrinth.hero == self.labyrinth.guardian:
            if result == 3:
                print ("**You Win**")
            elif result != 3:
                print ("**You Loose**")
