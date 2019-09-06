import pygame
import constants
from position import Position

class Display:

    def __init__(self,labyrinthe):

        self.labyrinthe = labyrinthe
        self._running = True
    
    def on_event(self):

        if event.type == pygame.QUIT:
            self._running = False
        
    
    def init_display(self):
        
        self.window = pygame.display.set_mode((constants.HEIGHT, constants.WIDTH))
        self.background = pygame.image.load(constants.BACKGROUND)
        self.labyrinthe.wall = pygame.image.load(constants.WALL)
        self.labyrinthe.mcgyver = pygame.image.load(constants.MCGYVER)
        self.labyrinthe.window.blit(self.background,(0,0))
    
    def close_display(self):

        pygame.quit()
                

        

   
      

