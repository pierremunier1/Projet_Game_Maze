from position import Position



class Labyrinthe:

    def __init__(self):

        self.start = None
        self.end = None
        self.player = None
        self.width = None
        self.height = None
        self.passages = []
        self.mur = []
    
    def build(self,filename):
        
        with open(filename) as laby:
            for n_line, line in enumerate(laby):
                for n_column, c in enumerate(line):
                    position = Position(n_column, n_line)
                    if c == "S":
                        self.passages.append(position)
                        self.start = position
                    elif c == "E":
                        self.passages.append(position)
                        self.end = position
                    elif c == "P":
                        self.passages.append(position)
                        self.player = position
                    elif c == ".":
                        self.passages.append(position)
                    elif c == "#":
                        self.mur.append(position)
                    
            self.width = n_column + 1
            self.height = n_line + 1
        print()

    def move(self):
        
            direction = input('direction: up,down,left,right: ')
            if direction == 'down':
                if self.player.down() in self.passages:
                    self.player = self.player.down()
                else:
                    print('***direction non valide !!!***')
            elif direction == 'up':
                if self.player.up() in self.passages:
                    self.player = self.player.up()
                else:
                    print('***direction non valide !!!***')
            elif direction == 'right':
                if self.player.right() in self.passages:
                    self.player = self.player.right()
                else:
                    print('***direction non valide !!!***')
            elif direction == 'left':
                if self.player.left() in self.passages:
                    self.player = self.player.left()
                else:
                    print('***direction non valide !!!***')

        
    def show(self):
        
        for y in range(self.height):
            for x in range(self.width):
                position = Position(x, y)
                if position == self.start:
                    print("S",end='')
                elif position == self.player:
                    print("P",end='')
                elif position == self.end:
                    print("E",end='')
                elif position in self.passages:
                    print(".",end='')
                elif position in self.mur:
                    print("#",end='')
            print()


            


           



                        

