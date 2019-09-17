import pygame
import constants
from position import Position

class Display:

    def __init__(self,labyrinthe):

        self.labyrinthe = labyrinthe
    
    def init_display(self):
        
        """initializing pygame variables"""
        
        "==WINDOW=="

        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(constants.WINDOW_TITLE)
        icon = pygame.image.load(constants.MCGYVER)
        pygame.display.set_icon(icon)
        self.window = pygame.display.set_mode((constants.HEIGHT, constants.WIDTH)) 
        self.black_bg = pygame.Surface((constants.HEIGHT, constants.WIDTH))
        self.black_bg.fill((constants.BG_COLOR))
        self.background = pygame.image.load(constants.BACKGROUND)
        self.wall = pygame.image.load(constants.WALL)

        "==SOUND=="

        pygame.mixer.music.load(constants.INTRO)
        pygame.mixer.music.play()
    
        "==CHARACTER & ITEMS=="
        
        self.mcgyver = pygame.image.load(constants.MCGYVER).convert_alpha()
        self.mcgyver_dead = pygame.image.load(constants.MCGYVER_DEAD).convert_alpha()
        self.guardian = pygame.image.load(constants.GUARDIAN).convert_alpha()
        self.end = pygame.image.load(constants.END).convert_alpha()
        self.ether = pygame.image.load(constants.ETHER).convert_alpha()
        self.tube = pygame.image.load(constants.TUBE).convert_alpha()
        self.needle = pygame.image.load(constants.NEEDLE).convert_alpha()
        

    def update_display(self):

        """Method refresh display"""
        
        self.window.blit(self.black_bg,(constants.BG_COLOR_POSITION))
        self.window.blit(self.background,(constants.BG_POSITION))
        
        
    def show_display(self):
        
        """Method showing the maze at the screen and all character and items"""

        for y in range(self.labyrinthe.height):
            for x in range(self.labyrinthe.width):
                position = Position(x, y)
                if position in self.labyrinthe.wall:
                    self.window.blit(self.wall,(x*constants.SPRITE_SIZE,y*constants.SPRITE_SIZE))
                elif position == self.labyrinthe.hero:
                    self.window.blit(self.mcgyver,(x*constants.SPRITE_SIZE,y*constants.SPRITE_SIZE))
                elif position == self.labyrinthe.guardian:
                    self.window.blit(self.guardian,(x*constants.SPRITE_SIZE,y*constants.SPRITE_SIZE))
                elif position == self.labyrinthe.end:
                    self.window.blit(self.end,(x*constants.SPRITE_SIZE,y*constants.SPRITE_SIZE))   
                elif position in self.labyrinthe.ether:
                    self.window.blit(self.ether,(x*constants.SPRITE_SIZE,y*constants.SPRITE_SIZE))
                elif position in self.labyrinthe.needle:
                    self.window.blit(self.needle,(x*constants.SPRITE_SIZE,y*constants.SPRITE_SIZE))
                elif position in self.labyrinthe.tube:
                    self.window.blit(self.tube,(x*constants.SPRITE_SIZE,y*constants.SPRITE_SIZE))
                


    def catch_items_gui(self):

        """Method that allows MacGyver to take the objects in the maze"""
        
        font = pygame.font.SysFont(constants.FONT_POLICE, constants.FONT_SIZE , bold=1)
        self.result = len(self.labyrinthe.inventory)
        self.text = font.render("items: " + str(self.result), 1, (constants.FONT_COLOR)) 
        self.window.blit(self.text,(constants.FONT_POSITION))
       
        
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
            
        elif self.labyrinthe.hero == self.labyrinthe.guardian:

            if self.result == constants.RESULT:
                self.win = font.render((constants.WIN),1,(constants.FONT_COLOR))
                self.window.blit(self.win,(constants.FONT_RESULT_POSITION))
                self.win
                self.labyrinthe.free.append(self.labyrinthe.end)    
            
            else:
                self.loose = font.render((constants.LOOSE),1,(constants.FONT_COLOR))
                self.mcgyver = self.mcgyver_dead
                self.window.blit(self.loose,(constants.FONT_RESULT_POSITION))
                self.loose
                self.labyrinthe.wall.pop()
                
             
              