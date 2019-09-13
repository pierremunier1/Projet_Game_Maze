"""Game constants"""
from pathlib import Path
import pygame

BASE_DIR = Path(__file__).resolve().parent

HEIGHT = 420
WIDTH = 480
POSITION_ITEMS = [(0,450),(30,450),(60,450)]

sprite_size = 30

WALL = str(BASE_DIR/'pictures'/'mur_1.png')
INV = str(BASE_DIR/'pictures'/'inv.png')
HOME = str(BASE_DIR/'pictures'/'home.png')
FREE = str(BASE_DIR/'pictures'/'free.png')
BACKGROUND = str(BASE_DIR/'pictures'/'back_1.png')
MCGYVER = str(BASE_DIR/'pictures'/'MacGyver.png')
GUARDIAN = str(BASE_DIR/'pictures'/'guardian.png')
NEEDLE = str(BASE_DIR/'pictures'/'needle.png')
ETHER = str(BASE_DIR/'pictures'/'ether.png')
TUBE = str(BASE_DIR/'pictures'/'tube.png')
