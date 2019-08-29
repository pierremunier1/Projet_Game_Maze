from labyrinthe import Labyrinthe
from random import sample
from position import Position

class Items:


    def __init__(self,labyrinthe):

        self.inventory = 0
        self.labyrinthe = labyrinthe


    def random_position(self):
        
        print(sample(self.labyrinthe.passages, k=3))
        self.labyrinthe.random_items = (sample(self.labyrinthe.passages, k=3))
