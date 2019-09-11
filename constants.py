"""Game constants"""
from pathlib import Path
import pygame

BASE_DIR = Path(__file__).resolve().parent

HEIGHT = 420
WIDTH = 500

sprite_size = 30

WALL = str(BASE_DIR/'pictures'/'mur.png')
HOME = str(BASE_DIR/'pictures'/'home.png')
BACKGROUND = str(BASE_DIR/'pictures'/'back.jpg')
MCGYVER = str(BASE_DIR/'pictures'/'MacGyver.png')
NEEDLE = str(BASE_DIR/'pictures'/'needle.png')
ETHER = str(BASE_DIR/'pictures'/'ether_1.png')
TUBE = str(BASE_DIR/'pictures'/'tube.png')

"""Inventory"""

x_inventory = 400