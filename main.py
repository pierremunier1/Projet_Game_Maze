from labyrinthe import Labyrinthe
from position import Position
from hero import Hero

class Game:

        def __init__(self):

                self.labyrinthe = Labyrinthe()
                self.labyrinthe.build('laby.txt')
                self.hero = Hero(self.labyrinthe)
                

        def choice(self):
                
                direction = input ('***choisir direction : ')              
                if direction == "down":
                        self.hero.move(direction)     
                elif direction == "up":
                        self.hero.move(direction)
                elif direction == "left":
                        self.hero.move(direction)
                elif direction == "right":
                        self.hero.move(direction)
                                                
def main():
        game = Game()

        while  1<5 :

                game.labyrinthe.show()
                game.choice()
             

if __name__ == "__main__":
        main()