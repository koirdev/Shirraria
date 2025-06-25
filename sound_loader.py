import pygame
from config import *

# load music
if MUSIC == 1:
    pygame.mixer.music.load('assets/sound/Slower-Tempo-2020-03-22_-_8_Bit_Surf_-_FesliyanStudios.com_-_David_Renda.mp3')
    pygame.mixer.music.play(-1)