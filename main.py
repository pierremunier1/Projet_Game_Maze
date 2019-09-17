from labyrinth import Maze
from position import Position
from random import sample
from hero import Hero
from Items import Items




class Game:
 
        def __init__(self):

                self.labyrinth = Labyrinth()
                self.labyrinth.build('laby.txt')
                self.hero = Hero(self.labyrinth)
                self.items = Items(self.labyrinth)
               
              
                

        def choice(self):
                
                direction = input ('***choose direction : ')   
                select = ("up","down","left","right")
                if direction in select:
                        self.hero.move(direction)
                
        
def main():

        game = Game()
        game.items.add_random_position()
        
        
        

        while  1<5 :

                game.labyrinth.show()
                game.choice()
                game.hero.catch_items()
                game.hero.result_inventory()
               
             

if __name__ == "__main__":
        main()