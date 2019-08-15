
from position import Position

class Hero:

    def __init__(self,labyrinthe):

        self.labyrinthe = labyrinthe
    

    def move(self,direction):

        new_position = getattr(self.labyrinthe.hero,direction)()
        if new_position in self.labyrinthe.passages:
            self.labyrinthe.hero = new_position
        else:
            print('***position non valide***')
            
            
            


    
        
 

        

        
    
