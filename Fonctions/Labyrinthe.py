
from .Joueur import Joueur

class Labyrinthe:

 
    def __init__(self,level):

        self.level = "level.txt"

            

    def show_labyrinthe(self,n_ligne,level,pos_hero,perso):

        """affichage du labyrinthe lors de la lecture du fichier txt"""

        self.perso = perso
        self.pos_hero = pos_hero

        n_ligne = 0
        
        with open(self.level, "r") as level:
            
            for ligne in level:
                
                if  n_ligne == pos_hero[1] :
                    
                        print(ligne[0:pos_hero[0]] + perso + ligne [pos_hero[0]+1])

                else :
                        print (ligne)
                        n_ligne = n_ligne +1

if __name__ == "__main__":
    lab = Labyrinthe()
    joueur = Joueur()
    lab.show_labyrinthe