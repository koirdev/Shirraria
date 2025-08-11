import pygame
from config import *

pygame.mixer.init()

# load music
if MUSIC == 1:
    pygame.mixer.music.load('assets/sound/Slower-Tempo-2020-03-22_-_8_Bit_Surf_-_FesliyanStudios.com_-_David_Renda.mp3')
    pygame.mixer.music.play(-1)

# Load sound effects
if SFX == 1:
    clickSound = pygame.mixer.Sound('assets/sfx/click.wav')
    click2Sound = pygame.mixer.Sound('assets/sfx/click2.wav')
    whooshSound = pygame.mixer.Sound('assets/sfx/whoosh.wav')

laughSound = pygame.mixer.Sound('assets/sfx/laugh.wav')
