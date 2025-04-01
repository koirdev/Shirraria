import pygame
from config import WINDOW_MODE, WIDTH, HEIGHT
from message_box import WindowModeError


def CheckWindowMode():
    # Window Mode Error
        if WINDOW_MODE != 0 or 1 or 2 or 3:
            WindowModeError()
            exit()