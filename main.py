from labyrinthe import Labyrinthe
from position import Position
from random import sample
from hero import Hero

class Game:

        def __init__(self):

                self.labyrinthe = Labyrinthe()
                self.labyrinthe.build('laby.txt')
                self.hero = Hero(self.labyrinthe)
                
                

        def choice(self):
                
                select = input ('***choisir direction : ')
                direction = select       
                if select in direction:
                        self.hero.move(direction)    

                                               
def main():

        game = Game()

        while  1<5 :

                game.labyrinthe.show()
                game.choice()
               
             

if __name__ == "__main__":
        main()