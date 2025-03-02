import pygame
from config import FULLSCREEN, DEFAULT_WINDOW, RESIZABLE_WINDOW, HARDWARE_RENDER, WIDTH, HEIGHT
from message_box import WindowModeError


def CheckWindowMode():
    if RESIZABLE_WINDOW == 1:
        window = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)

    # Window Mode Error
    if RESIZABLE_WINDOW == 1:
        if FULLSCREEN == 1:
            if DEFAULT_WINDOW == 1:
                WindowModeError()
                exit()
    if RESIZABLE_WINDOW == 1:
        if FULLSCREEN == 1:
            WindowModeError()
            exit()
    if RESIZABLE_WINDOW == 1:
        if DEFAULT_WINDOW == 1:
            WindowModeError()
            exit()
    if FULLSCREEN == 1:
        if DEFAULT_WINDOW == 1:
            WindowModeError()
            exit()