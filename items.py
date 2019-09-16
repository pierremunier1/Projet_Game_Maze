
from position import Position
from random import sample
import constants

class Items:

    def __init__(self,labyrinthe):

        self.labyrinthe = labyrinthe
        self.labyrinthe.items = self.random()
        
    def random(self):

        return sample(self.labyrinthe.passages, constants.RANDOMS_ITEMS)
        

    def add_random_position(self):

        self.labyrinthe.ether.append(self.labyrinthe.items[0])
        self.labyrinthe.tube.append(self.labyrinthe.items[1])
        self.labyrinthe.needle.append(self.labyrinthe.items[2])
        



   