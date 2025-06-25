import pygame
from config import *
from splashes import random_splash

pygame.init()

# Fonts
font = pygame.font.Font('assets/fonts/42dotSans-Bold.ttf', 27)
pause_tips_font = pygame.font.Font('assets/fonts/42dotSans-Bold.ttf', 25)
pause_font = pygame.font.Font('assets/fonts/42dotSans-Bold.ttf', 55)
if SPLASHES == 1:
    splash_text = pygame.font.Font('assets/fonts/Nepoboy-MVMaB.otf', 25)
credits_font = pygame.font.Font('assets/fonts/MotleyForcesRegular-w1rZ3.ttf', 30)
menu_font = pygame.font.Font('assets/fonts/ArchivoBlack-Regular.ttf', 35)
level_select_title_font = pygame.font.Font('assets/fonts/ArchivoBlack-Regular.ttf', 55)

# Text
if SPLASHES == 1:
    splash_text = splash_text.render(random_splash,False,(245, 224, 86))

build_info_text = font.render("ver. "+VERSION,False,(252, 250, 250))
level_select_title_text = level_select_title_font.render("Level Select",False,(252,250,250))
if WARNING_TEXT == 1:
    warning_text = font.render("This build is unstable!",False,(252, 250, 250))
help_text = font.render("Available on GitHub",False,(252, 250, 250))
youtube_text = font.render("YouTube:",False,(252,250,250))
github_text = font.render("GitHub:",False,(252,250,250))
gamejolt_text = font.render("Game Jolt:",False,(252,250,250))
pause_title_text = pause_font.render("Pause", False, (252,250,250))
pause_tips_text1 = pause_tips_font.render("Press P to contiune", False, (252,250,250))
pause_tips_text2 = pause_tips_font.render("Press BACKSPACE to return to the main menu", False, (252,250,250))
pause_not_founded = pause_tips_font.render("Level not founded", False, (252,250,250))



# Debug Text
if DEBUG_MODE == 1:
    if WINDOW_MODE == 2: #fullshit mode
        fullscreen_text = font.render("FULLSCREEN_MODE", False,(252,250,250))
    if WINDOW_MODE == 1: # res shit
        resizable_text = font.render("RESIZABLE_MODE", False,(252,250,250))
    if WINDOW_MODE == 3: # hardware win
        hardware_render_text = font.render("HARDWARE_RENDER_MODE", False,(252,250,250)) 
    if WINDOW_MODE == 0: # def win
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
  build_info_text = font.render("TESTER_MODE - "+"ver. "+VERSION,False,(252,250,250))
if DEBUG_MODE == 1:
  build_info_text = font.render("DEBUG_MODE - "+"ver. "+VERSION,False,(252,250,250))

