from labyrinthe import Labyrinthe
from random import sample

class Items:


    def __init__(self,labyrinthe):

        self.inventory = 0
        self.labyrinthe = labyrinthe


    def generate_items(self):
        
        print(sample(self.labyrinthe.passages,k=3))
       
