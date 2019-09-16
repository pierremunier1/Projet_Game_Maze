from position import Position
from items import Items
import constants


class Labyrinthe:

    def __init__(self):

       
        self.start = None
        self.end = None
        self.hero = None
        self.width = None
        self.height = None
        self.guardian = None
        self.passages = []
        self.mur = []
        self.ether = []
        self.tube = []
        self.needle = []
        self.items = []
        self.inventory = []
    
        
    def build(self,filename):
        

        with open(filename) as laby:
            for n_line, line in enumerate(laby):
                for n_column, c in enumerate(line):
                    position = Position(n_column, n_line)
                    if c == "S":
                        self.passages.append(position)
                        self.start = position
                    elif c == "E":
                        self.end = position
                    elif c == "P":
                        self.passages.append(position)
                        self.hero = position                       
                    elif c == ".":
                        self.passages.append(position)
                    elif c == "#":
                        self.mur.append(position)
                    elif c == "G":
                        self.guardian = position
                        self.passages.append(position) 
         
            self.width = n_column + 1
            self.height = n_line + 1

        print()

    def show(self):
        
    
        for y in range(self.height):
            for x in range(self.width):
                position = Position(x, y)
                if position == self.start:
                    print("S",end='')
                elif position in self.ether:
                    print("€",end='')
                elif position in self.needle:
                    print("N",end='')
                elif position in self.tube:
                    print("T",end='')
                elif position == self.hero:
                    print("P",end='')
                elif position == self.guardian:
                    print("G",end='')
                elif position == self.end:
                    print("E",end='')
                elif position in self.passages:
                    print(".",end='')
                elif position in self.mur:
                    print("#",end='')

            print()
            
            
        
    

            


           



                        

