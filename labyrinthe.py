from position import Position
from random import sample
from Items import Items
from display_gui import Display
import constants
import pygame
import os


class Labyrinthe:

    def __init__(self):

       
        self.start = None
        self.end = None
        self.hero = Position
        self.width = None
        self.height = None
        self.guard = None
        self.wall = None
        self.passages = []
        self.mur = []
        self.ether = []
        self.tube = []
        self.needle = []
        self.items = []
        
        #Display Init 

        self.window = pygame.display.set_mode((constants.HEIGHT, constants.WIDTH))
        self.mcgyver = None
        self.wall = None
        
    def build(self,filename):
        

        with open(filename) as laby:
            for n_line, line in enumerate(laby):
                for n_column, c in enumerate(line):
                    position = Position(n_column, n_line)
                    if c == "S":
                        self.passages.append(position)
                        self.start = position
                    elif c == "E":
                        self.passages.append(position)
                        self.end = position
                    elif c == "P":
                        self.passages.append(position)
                        self.hero = position                       
                    elif c == ".":
                        self.passages.append(position)
                    elif c == "#":
                        self.mur.append(position)
                    elif c == "G":
                        self.guard = position
                        self.passages.append(position)
                    
                    
            self.width = n_column + 1
            self.height = n_line + 1

        print()

    def show(self):
        
        self
        
        for y in range(self.height):
            for x in range(self.width):
                position = Position(x, y)
                if position == self.start:
                    print("S",end='')
                elif position in self.ether:
                    print("€",end='')
                elif position in self.needle:
                    print("N",end='')
                elif position in self.tube:
                    print("T",end='')
                elif position == self.hero:
                    self.window.blit(self.mcgyver,(position.x,position.y))
                    print("P",end='')
                elif position == self.guard:
                    print("G",end='')
                elif position == self.end:
                    print("E",end='')
                elif position in self.passages:
                    print(".",end='')
                elif position in self.mur:
                    self.window.blit(self.wall,(position.x,position.y,30,30))
                    print("#",end='')
            print()
            pygame.display.update()

            
        
    

            


           



                        

