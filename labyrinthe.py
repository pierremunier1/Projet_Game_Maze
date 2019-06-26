# **Help MacGyver to escape**

#import pygame module

import pygame
from pygame.locals import *

pygame.init()

#Open Window
window = pygame.display.set_mode((640, 480))

#load background
background = pygame.image.load("pictures/background.jpg").convert()
window.blit(background, (0,0))

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
	        continuer = 0