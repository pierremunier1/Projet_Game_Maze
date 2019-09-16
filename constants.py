"""Game constants"""
from pathlib import Path
import pygame

"==PATHS_INIT=="

BASE_DIR = Path(__file__).resolve().parent

"==PLAYER=="

MCGYVER = str(BASE_DIR/'pictures'/'MacGyver.png')
WIN = "You win! You can escape!"
LOOSE = "You loose! You can't escape!"


"==ITEMS=="

RANDOMS_ITEMS = K=3
RESULT = 3
GUARDIAN = str(BASE_DIR/'pictures'/'guardian.png')
END = str(BASE_DIR/'pictures'/'end.png')
NEEDLE = str(BASE_DIR/'pictures'/'needle.png')
ETHER = str(BASE_DIR/'pictures'/'ether.png')
TUBE = str(BASE_DIR/'pictures'/'tube.png')
POSITION_ITEMS = [(0,450),(30,450),(60,450)]

"==WINDOW=="

HEIGHT = 420
WIDTH = 480
BG_POSITION = (0,0)
BG_COLOR = (0,0,0)
BG_COLOR_POSITION = (110,455)
WINDOW_TITLE = 'MacGyver Escape Game'
WALL = str(BASE_DIR/'pictures'/'mur_1.png')
BACKGROUND = str(BASE_DIR/'pictures'/'back_1.png')
SPRITE_SIZE = 30

"==SOUND=="

INTRO = str(BASE_DIR/'sound'/'macgyver.mid')

"==FONTS=="

FONT_RESULT_POSITION = (180,455)
FONT_POSITION = (110,455)
FONT_COLOR = (255,255,255)
FONT_SIZE = 16
FONT_POLICE = "arial"
