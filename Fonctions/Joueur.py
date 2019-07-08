
class Joueur:

    def __init__(self,dep):

        self.dep = dep

    def choix_joueur(self,level,pos_hero,dep,verification_deplacement):
        
        choix = input("déplacement (Haut/Bas/Droite/Gauche/Quitter) ? ")
        
        if choix == "H" or choix == "Haut" : 
            
            dep = verification_deplacement(level, pos_hero[0], pos_hero[1] -1)
            
        elif choix == "B" or choix == "Bas" :
                
            dep = verification_deplacement(level, pos_hero[0], pos_hero[1] +1)
                
        elif choix == "G" or choix == "Gauche" :
                    
            dep = verification_deplacement(level, pos_hero[0] -1, pos_hero[1])

        elif choix == "D" or choix == "Droite" :


            dep = verification_deplacement(level, pos_hero[0] +1, pos_hero[1])

        elif choix == "Q" or choix == "Quitter" :
            
            if dep == None :
                
                print("Déplacement impossible")

        else:

            pos_hero[0] = dep[0]# modification du contenu de la liste
            pos_hero[1] = dep[1]# pos_hero