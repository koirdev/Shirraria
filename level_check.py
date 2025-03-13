from config import LEVEL

from message_box import LevelNotFounded
import pygame
from main import *
pygame.init()

def Level_Check():
	global Level_1

    if LEVEL == 1:
        Level_1()
EL
        running = False
        LevelNotFounded()
        exit()



