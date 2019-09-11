from position import Position
import pygame

class Hero:

    def __init__(self,labyrinthe):

        self.inventory = []
        self.labyrinthe = labyrinthe
        

    def move(self,direction):


        new_position = getattr(self.labyrinthe.hero,direction)()
        if new_position in self.labyrinthe.passages:
            self.labyrinthe.hero = new_position
        else:
            print('***invalid position***')
        
        

    def catch_items(self):

        if self.labyrinthe.hero in self.labyrinthe.ether:
            self.inventory.append(self.labyrinthe.ether)
            self.labyrinthe.ether = []

        elif self.labyrinthe.hero in self.labyrinthe.tube:
            self.inventory.append(self.labyrinthe.tube)
            self.labyrinthe.tube = []
            
        elif self.labyrinthe.hero in self.labyrinthe.needle:
            self.inventory.append(self.labyrinthe.needle)
            self.labyrinthe.needle = []
    

    def result_inventory(self):

        if self.labyrinthe.needle in self.inventory:
            self.labyrinthe.inventory_gui.append(self.labyrinthe.needle)
            self.window.blit(self.needle)
        result = len(self.inventory)
        
        print("Items:",result)
        if self.labyrinthe.hero == self.labyrinthe.guard:
            if result == 3:
                print("**You Win**")
            elif result != 3:
                print("**You Loose**")


            



    
        
 

        

        
    
