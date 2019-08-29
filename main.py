from labyrinthe import Labyrinthe
from position import Position
from random import sample
from hero import Hero
from items import Items

class Game:

        def __init__(self):

                self.labyrinthe = Labyrinthe()
                self.labyrinthe.build('laby.txt')
                self.hero = Hero(self.labyrinthe)
                self.random_items = Items(self.labyrinthe)
                
                

        def choice(self):
                
                direction = input ('***choisir direction : ')
                select = ("up","down","left","right")
                if direction in select:
                        self.hero.move(direction)
                
                
               

        

        
       


def main():

        game = Game()
        game.labyrinthe.random_position()
     

        while  1<5 :

                game.labyrinthe.show()
                game.choice()
               
             

if __name__ == "__main__":
        main()