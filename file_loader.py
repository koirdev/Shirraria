import pygame
from splashes import random_splash
from config import *

pygame.init()


# Fonts
font = pygame.font.Font('assets/fonts/funny_cute.ttf', 25)
pause_tips_font = pygame.font.Font('assets/fonts/funny_cute.ttf', 25)
pause_font = pygame.font.Font('assets/fonts/funny_cute.ttf', 55)
if SPLASHES == 1:
    splash_text = pygame.font.Font('assets/fonts/Nepoboy-MVMaB.otf', 25)
credits_font = pygame.font.Font('assets/fonts/MotleyForcesRegular-w1rZ3.ttf', 30)
menu_font = pygame.font.Font('assets/fonts/ArchivoBlack-Regular.ttf', 35)
level_select_title_font = pygame.font.Font('assets/fonts/ArchivoBlack-Regular.ttf', 55)

# Text
if SPLASHES == 1:
    splash_text = splash_text.render(random_splash,False,(245, 224, 86))

build_info_text = font.render(VERSION,False,(252, 250, 250))
level_select_title_text = level_select_title_font.render("Level Select",False,(252,250,250))
if DISTRIBUTE_TEXT == 1:
    distribute_text = font.render("DO NOT DISTRIBUTE",False,(252, 250, 250))
help_text = font.render("'Q' - quit '7' - screenshot 'F1' - Volume off 'F2' - Volume on ",False,(252, 250, 250))
boosty_text = font.render("Boosty:",False,(252,250,250))
youtube_text = font.render("YouTube:",False,(252,250,250))
github_text = font.render("GitHub:",False,(252,250,250))
gamejolt_text = font.render("GameJolt:",False,(252,250,250))
pause_title_text = pause_font.render("Pause", False, (252,250,250))
pause_tips_text1 = pause_tips_font.render("Press P to contiune", False, (252,250,250))
pause_tips_text2 = pause_tips_font.render("Press BACKSPACE to return to the main menu", False, (252,250,250))
pause_not_founded = pause_tips_font.render("Level not founded", False, (252,250,250))

# Debug Text
if DEBUG_MODE == 1:
    if FULLSCREEN == 1:
        fullscreen_text = font.render("FULLSCREEN_MODE", False,(252,250,250))
    if RESIZABLE_WINDOW == 1:
        resizable_text = font.render("RESIZABLE_MODE", False,(252,250,250))
    if HARDWARE_RENDER == 1:
        hardware_render_text = font.render("HARDWARE_RENDER_MODE", False,(252,250,250)) 
    if DEFAULT_WINDOW == 1:
        default_window_text = font.render("DEFAULT_WINDOW_MODE", False,(252,250,250))

# Credits Info
credits_title = credits_font.render("Shirraria Credits:",False,(252,250,250))
credits_koirdev = credits_font.render("koirdev - Programmer, Artist, Composer",False,(252,250,250))
credits_venux = credits_font.render("VENUX - Tester",False,(252,250,250))
credits_JBoT = credits_font.render("James BoT - Tester",False,(252,250,250))
credits_motver = credits_font.render("MOTVER - Tester",False,(252,250,250))


# Checking the modes
if DEV_MODE == 1:
  build_info_text = font.render("DEV_MODE",False,(252,250,250))
if TEST_MODE == 1:
  build_info_text = font.render("TESTER_MODE - "+VERSION,False,(252,250,250))
if DEBUG_MODE == 1:
  build_info_text = font.render("DEBUG_MODE - "+VERSION,False,(252,250,250))

# load images
character_img = pygame.image.load('assets/images/player.png')
shirLogo = pygame.image.load('assets/images/shirLogo.png')
bg = pygame.image.load('assets/images/bg.png')
boosty_logo = pygame.image.load('assets/images/boosty_logo.png')
youtube_logo = pygame.image.load('assets/images/youtube_logo.png')
github_logo = pygame.image.load('assets/images/github_logo.png')
gamejolt_logo = pygame.image.load('assets/images/gamejolt_logo.png')
credits = pygame.image.load('assets/images/credits_sign.png')
grass_img = pygame.image.load('assets/images/grass.png')
door1 = pygame.image.load('assets/images/skull_door.png')

# Resizing images
shirLogo = pygame.transform.scale(shirLogo, (430, 170))
bg = pygame.transform.scale(bg, (1500, 750))
boosty_logo = pygame.transform.scale(boosty_logo, (100, 100))
youtube_logo = pygame.transform.scale(youtube_logo, (125, 150))
github_logo = pygame.transform.scale(github_logo, (100, 100))
gamejolt_logo = pygame.transform.scale(gamejolt_logo, (100, 100))
credits_sign_img = pygame.transform.scale(credits, (650, 500))
character_img = pygame.transform.scale(character_img,(100,200))
grass_img = pygame.transform.scale(grass_img, (1400,220))
door1 = pygame.transform.scale(door1, (190, 400))

# load music
if MUSIC == 1:
    pygame.mixer.music.load('assets/sound/Slower-Tempo-2020-03-22_-_8_Bit_Surf_-_FesliyanStudios.com_-_David_Renda.mp3')
    pygame.mixer.music.play(-1)