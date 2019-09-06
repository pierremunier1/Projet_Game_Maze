from labyrinthe import Labyrinthe
from position import Position
from random import sample
from hero import Hero
from Items import Items
from display_gui import Display
import constants
import pygame



class Game:
 
        def __init__(self):

            self.labyrinthe = Labyrinthe()
            self.labyrinthe.build('laby.txt')
            self.hero = Hero(self.labyrinthe)
            self.items = Items(self.labyrinthe)
            self.display_guy = Display(self.labyrinthe)

            
                
              
        

        def choice(self):
                
            direction = input ('***choose direction : ')   
            select = ("up","down","left","right")
            if direction in select:
                    self.hero.move(direction)




                
        
def main():

        game = Game()
        game.items.add_random_position()
        game.display_guy.init_display()
        pygame.init()
        

        while  1<5 :

                game.labyrinthe.show()
                game.choice()
                game.hero.catch_items()
                game.hero.result_inventory()
               
             

if __name__ == "__main__":
        main()