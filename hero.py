from position import Position

class Hero:

    def __init__(self,labyrinthe):

        self.inventory = []
        self.labyrinthe = labyrinthe
        

    def move(self,direction):

        new_position = getattr(self.labyrinthe.hero,direction)()
        if new_position in self.labyrinthe.passages:
            self.labyrinthe.hero = new_position
        else:
            print('***position non valide***')

    def catch_items(self):

        
        if self.labyrinthe.hero in self.labyrinthe.ether:
            self.inventory.extend(self.labyrinthe.ether)
            self.labyrinthe.ether = []
        elif self.labyrinthe.hero in self.labyrinthe.tube:
            self.inventory.extend(self.labyrinthe.tube)
            self.labyrinthe.tube = []
        elif self.labyrinthe.hero in self.labyrinthe.needle:
            self.inventory.extend(self.labyrinthe.needle)
            self.labyrinthe.needle = []
        
    def result_inventory(self):

        result = len(self.inventory)
        print("compteur:",result)
        if result == 3:
            print("**victoire**")
            


            



    
        
 

        

        
    
