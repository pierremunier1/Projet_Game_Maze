import os


level_1 = [
 "+-------------------+",
 "|                   |",
 "|                   |",
 "|                   |",
 "|                   |",
 "|                   |",
 "|                   |",
 "|                   |",
 "|                   |",              
 "|                   |",
 "|                   |",
 "|                   |",
 "+-------------------+",
]

def show_labyrinthe(lab,perso,pos_hero):
    n_ligne = 0
    for ligne in lab:
        if  n_ligne == pos_hero[1] : 
           # ne s’exécute que si le test est vrai
            print(ligne[0:pos_hero[0]] + perso + ligne [pos_hero[0]+1])
        else :
            print(ligne)
        n_ligne = n_ligne +1


def verification_deplacement(lab, pos_col, pos_ligne): 
    """Indique si le déplacement du personnage est autorisé ou pas.
    lab : LabyrintheB
    pos_ligne : position du personnage sur les lignes
    pos_col : position du personnage sur les colonnes
    Valeurs de retour :None : déplacement interdit
    [col, ligne] : déplacement autorisé sur la case indiquéepar la liste"""
    # Calcul de la taille du labyrinthe
    n_cols = len(lab[0])
    n_lignes = len(lab)
    # Teste si le déplacement conduit le personnage en dehors de l’aire
    # # de jeu
    if pos_ligne < 0 or pos_col < 0 or pos_ligne > (n_lignes -1)or\
        pos_col > (n_cols -1) :
        #le symbole \ indique que la ligne n’est pas terminée
        return None 
    elif lab[pos_ligne][pos_col] != " " :
        return None 
    else :
        return[pos_col, pos_ligne]

def choix_joueur(lab, pos_hero):
    """
    Interface avec l'utilisater & vérification si le déplacement est possible.
    """
    choix = input("Votre déplacement (Haut/Bas/Droite/Gauche/Quitter) ? ")

    if choix == "H"or choix == "Haut" : 
        dep = verification_deplacement(lab, pos_hero[0], pos_hero[1] -1)
    elif choix == "B"or choix == "Bas" : 
        dep = verification_deplacement(lab, pos_hero[0], pos_hero[1] +1)
    elif choix == "G"or choix == "Gauche" :
        dep = verification_deplacement(lab, pos_hero[0] -1, pos_hero[1])
    elif choix == "D"or choix == "Droite" :
        dep = verification_deplacement(lab, pos_hero[0] +1, pos_hero[1])
    elif choix == "Q"or choix == "Quitter" :os._exit(1)
    
    if dep == None :
            print("Déplacement impossible")
    else:
            pos_hero[0] = dep[0]# modification du contenu de la liste
            pos_hero[1] = dep[1]# pos_perso

def jeu(level, perso, pos_hero):

    while True :
        show_labyrinthe (level, perso, pos_hero)
        choix_joueur(level,pos_hero)            

########### 
# Programme principal 
# Initialisation du personnage
perso = "X"
pos_hero = [1,1]
# Lancement de la partie
jeu(level_1, perso, pos_hero)
