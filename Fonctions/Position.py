
class Position:

    """ définition de la position et vérification dans le tableau la position"""

    def __init__ (self, pos_col, pos_ligne,n_cols):

        self.position_x = pos_col
        self.position_y = pos_ligne
        self.n_cols = n_cols

    def verification_deplacement(self,level, pos_col, pos_ligne, n_cols): 
        
        n_lignes = len(level)
        if pos_ligne < 0 or pos_col < 0 or pos_ligne > (n_lignes -1)or\
            pos_col > (n_cols -1) :

            return None 

        elif level[pos_ligne][pos_col] != " " :
            
            return None 
        else :
            
            return[pos_col, pos_ligne]