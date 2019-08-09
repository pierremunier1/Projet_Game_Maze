from labyrinthe import Labyrinthe
from position import Position
from hero import Hero

class Game:
        
        def __init__(self):

                self.labyrinth = Labyrinthe()
                self.labyrinth.build("laby.txt")
                self.hero = Hero(self.labyrinth)
    





def main():

    
    labyrinth = Labyrinthe()
    labyrinth.build("laby.txt")
    
    

    while 1 < 5: 
        labyrinth.show()
        labyrinth.move()
    
    

if __name__ == "__main__":
    main()
