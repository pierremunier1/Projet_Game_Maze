import pygame
import constants
from position import Position

class Display:

    def __init__(self,labyrinthe):

        self.labyrinthe = labyrinthe
        self._running = True
    
    def init_display(self):
        
        pygame.init()
        pygame.time.Clock().tick(40)
        
    
        self.window = pygame.display.set_mode((constants.HEIGHT, constants.WIDTH))
        self.home = pygame.image.load(constants.HOME)
        self.background = pygame.image.load(constants.BACKGROUND)
        self.window.blit(self.background,(0,0))

        self.wall = pygame.image.load(constants.WALL)
        self.mcgyver = pygame.image.load(constants.MCGYVER)
        self.ether = pygame.image.load(constants.ETHER).convert()
        self.tube = pygame.image.load(constants.TUBE).convert()
        self.needle = pygame.image.load(constants.NEEDLE).convert()


    def home_screen(self):

        self.window.blit(self.home,(0,-50))
        FONT = pygame.font.Font(None, 30)
        TEXT_HOME = FONT.render( "Press ENTER to continue or ECHAP to quit", 1, (0, 0, 0))
        self.window.blit(TEXT_HOME,(20, 40))
        pygame.display.update()

    def update_display(self):

        self.window.blit(self.background,(0,0))
        return pygame.display.flip()

    def show_display(self):
        

        for y in range(self.labyrinthe.height):
            for x in range(self.labyrinthe.width):
                position = Position(x, y)
                if position in self.labyrinthe.mur:
                    self.window.blit(self.wall,(x*constants.sprite_size,y*constants.sprite_size))
                elif position == self.labyrinthe.hero:
                    self.window.blit(self.mcgyver,(x*constants.sprite_size,y*constants.sprite_size))
                    pygame.display.flip()
                elif position in self.labyrinthe.ether:
                    self.window.blit(self.ether,(x*constants.sprite_size,y*constants.sprite_size))
                elif position in self.labyrinthe.needle:
                    self.window.blit(self.needle,(x*constants.sprite_size,y*constants.sprite_size))
                elif position in self.labyrinthe.tube:
                    self.window.blit(self.tube,(x*constants.sprite_size,y*constants.sprite_size))

    def result_inventory(self):

        if self.labyrinthe.needle in self.labyrinthe.inventory:
            self.labyrinthe.inventory_gui.append(self.labyrinthe.needle)
            self.window.blit(self.needle)
            pygame.display.flip()

            print(self.labyrinthe.inventory_gui)
        