from position import Position
from random import sample
import constants

class Items:

    """Class of the Items"""

    def __init__(self,labyrinthe):

        self.labyrinthe = labyrinthe
        self.labyrinthe.items = self.random()
        
    def random(self):

        """Method check random position items into the free position located in self.labyrinthe.free"""

        return sample(self.labyrinthe.free, constants.RANDOMS_ITEMS)
        

    def add_random_position(self):

        """Method add ramdom position for every items"""

        self.labyrinthe.ether.append(self.labyrinthe.items[0])
        self.labyrinthe.tube.append(self.labyrinthe.items[1])
        self.labyrinthe.needle.append(self.labyrinthe.items[2])
        



   