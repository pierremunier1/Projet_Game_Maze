"""Game constants"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

HEIGHT = 420
WIDTH = 480

#Game window's size
sprite_width_num = 15
sprite_height_num = 16 # +1 line to display MacGyver's inventory
sprite_size = 30

WALL = str(BASE_DIR/'pictures'/'mur.png')
BACKGROUND = str(BASE_DIR/'pictures'/'back.jpg')
MCGYVER = str(BASE_DIR/'pictures'/'MacGyver.png')


