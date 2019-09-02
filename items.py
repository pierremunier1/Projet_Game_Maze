from position import Position
from random import sample

class Items:

    def __init__(self,labyrinthe):

        self.labyrinthe = labyrinthe
        self.labyrinthe.ether = self.random()
        self.labyrinthe.tube = self.random()
        self.labyrinthe.needle = self.random()
    
    def random(self):

        return sample(self.labyrinthe.passages, k=1)



   