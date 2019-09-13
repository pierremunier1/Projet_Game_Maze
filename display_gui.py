import pygame
import constants
from position import Position

class Display:

    def __init__(self,labyrinthe):

        self.labyrinthe = labyrinthe
        self._running = True
    
    def init_display(self):
        
        pygame.init()
        pygame.font.init()
        pygame.time.Clock().tick(40)
        pygame.display.set_caption('MacGyver Escape Game')
       
        self.window = pygame.display.set_mode((constants.HEIGHT, constants.WIDTH)) 
        
        self.home = pygame.image.load(constants.HOME)
        self.background = pygame.image.load(constants.BACKGROUND)
        self.window.blit(self.background,(0,0))

        self.wall = pygame.image.load(constants.WALL)
        self.inv = pygame.image.load(constants.INV)
        self.mcgyver = pygame.image.load(constants.MCGYVER).convert_alpha()
        self.guardian = pygame.image.load(constants.GUARDIAN).convert_alpha()
        self.ether = pygame.image.load(constants.ETHER).convert_alpha()
        self.tube = pygame.image.load(constants.TUBE).convert_alpha()
        self.needle = pygame.image.load(constants.NEEDLE).convert_alpha()
        

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
                elif position == self.labyrinthe.guardian:
                    self.window.blit(self.guardian,(x*constants.sprite_size,y*constants.sprite_size))
                elif position in self.labyrinthe.ether:
                    self.window.blit(self.ether,(x*constants.sprite_size,y*constants.sprite_size))
                elif position in self.labyrinthe.needle:
                    self.window.blit(self.needle,(x*constants.sprite_size,y*constants.sprite_size))
                elif position in self.labyrinthe.tube:
                    self.window.blit(self.tube,(x*constants.sprite_size,y*constants.sprite_size))


        pygame.display.flip()
                    

    def catch_items_gui(self):

       
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        self.result = len(self.labyrinthe.inventory)
        textsurface = myfont.render(("Items:  %s" % self.result), True, (255, 255, 255))
        self.window.blit(textsurface,(110,445))
        
        

        if self.labyrinthe.hero in self.labyrinthe.ether:
            self.labyrinthe.inventory.append(self.labyrinthe.ether)
            self.window.blit(self.ether,(constants.POSITION_ITEMS.pop(0)))
            self.labyrinthe.ether = []
            
        elif self.labyrinthe.hero in self.labyrinthe.tube:
            self.labyrinthe.inventory.append(self.labyrinthe.tube)
            self.window.blit(self.tube,(constants.POSITION_ITEMS.pop(0)))
            self.labyrinthe.tube = []
            
        elif self.labyrinthe.hero in self.labyrinthe.needle:
            self.labyrinthe.inventory.append(self.labyrinthe.needle)
            self.window.blit(self.needle,(constants.POSITION_ITEMS.pop(0)))
            self.labyrinthe.needle = []
            
        pygame.display.update()





                    
      
 