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
                        
                
                keys = pygame.key.get_pressed()

                for event in pygame.event.get():
                        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                                pygame.quit()   
                        elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RIGHT:
                                        self.hero.move("right")
                                elif event.key == pygame.K_LEFT:
                                        self.hero.move("left")
                                elif event.key == pygame.K_DOWN:
                                        self.hero.move("down")
                                elif event.key == pygame.K_UP:
                                        self.hero.move("up")
                
       
        
def main():

        game = Game()
        game.items.add_random_position()
        game.display_guy.init_display() 
        game.hero.result_inventory()
        
        while  1<5 :

                game.display_guy.update_display()
                game.choice()
                game.display_guy.show_display()
                game.hero.catch_items()
                
if __name__ == "__main__":
        main()