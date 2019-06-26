# coding: utf-8

import pygame
from pygame.locals import *
import constants
import classes

def main():
	"""Main function of the MacGyver maze profram"""
	
	#Pygame initialization
pygame.init()

    
    #Game window properties
width = constants.sprite_width_num * constants.sprite_size
height = constants.sprite_height_num * constants.sprite_size
window = pygame.display.set_mode((width, height))
