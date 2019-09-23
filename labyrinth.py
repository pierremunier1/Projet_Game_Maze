from position import Position
from items import Items
import constants


class Maze:

    """Class for building and showing the maze"""

    def __init__(self):
        # initializing list and position of the maze

        self.start = None
        self.end = None
        self.hero = None
        self.width = None
        self.height = None
        self.guardian = None
        self.free = []
        self.wall = []
        self.ether = []
        self.tube = []
        self.needle = []
        self.items = []
        self.inventory = []

    def build(self, filename):
        # Method building the maze when reading the text file

        with open(filename) as laby:
            for n_line, line in enumerate(laby):
                for n_column, c in enumerate(line):
                    position = Position(n_column, n_line)
                    if c == "S":
                        self.free.append(position)
                        self.start = position
                    elif c == "E":
                        self.end = position
                    elif c == "P":
                        self.free.append(position)
                        self.hero = position
                    elif c == ".":
                        self.free.append(position)
                    elif c == "#":
                        self.wall.append(position)
                    elif c == "G":
                        self.guardian = position
                        self.free.append(position)

            self.width = n_column + 1
            self.height = n_line + 1

        print()

    def show(self):
        # Method display the maze in the terminal

        for y in range(self.height):
            for x in range(self.width):
                position = Position(x, y)
                if position == self.start:
                    print("S", end='')
                elif position in self.ether:
                    print("€", end='')
                elif position in self.needle:
                    print("N", end='')
                elif position in self.tube:
                    print("T", end='')
                elif position == self.hero:
                    print("P", end='')
                elif position == self.guardian:
                    print("G", end='')
                elif position == self.end:
                    print("E", end='')
                elif position in self.free:
                    print(".", end='')
                elif position in self.wall:
                    print("#", end='')

            print()
