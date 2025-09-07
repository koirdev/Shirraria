import pygame
from config import *

pygame.init()

# load images
character_img = pygame.image.load('assets/images/player.png')
shirLogo = pygame.image.load('assets/images/shirLogo.png')
bg = pygame.image.load('assets/images/bg.png')
youtube_logo = pygame.image.load('assets/images/youtube_logo.png')
github_logo = pygame.image.load('assets/images/github_logo.png')
gamejolt_logo = pygame.image.load('assets/images/gamejolt_logo.png')
credits = pygame.image.load('assets/images/credits_sign.png')
grass_img = pygame.image.load('assets/images/grass.png')
door1 = pygame.image.load('assets/images/skull_door.png')


# Resizing images
shirLogo = pygame.transform.scale(shirLogo, (430, 170))
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
youtube_logo = pygame.transform.scale(youtube_logo, (125, 150))
github_logo = pygame.transform.scale(github_logo, (100, 100))
gamejolt_logo = pygame.transform.scale(gamejolt_logo, (100, 100))
credits_sign_img = pygame.transform.scale(credits, (650, 500))
character_img = pygame.transform.scale(character_img,(100,200))
grass_img = pygame.transform.scale(grass_img, (1400,220))
door1 = pygame.transform.scale(door1, (190, 400))
