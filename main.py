from message_box import *
from config import * 
from screenshot import screen_shot
from file_loader import *
from check_window_mode import *
import pygame

# Checking init error
game_init = pygame.init()
if(game_init[1]>0):
    InitError()

# Window options
if FULLSCREEN == 1:
    window = pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN + pygame.SCALED)
else:

    if DEFAULT_WINDOW == 1:
        window = pygame.display.set_mode((WIDTH, HEIGHT))
    else:
        if HARDWARE_RENDER == 1:
            window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN + pygame.HWSURFACE + pygame.SCALED)
        else:
            WindowModeError()
            exit()

CheckWindowMode()


# Window title and icon
pygame.display.set_caption("Shirraria")
icon = pygame.image.load('assets/images/icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# Menu Sections
if DEBUG_MODE == 1:
    items = ['Level 1', 'Level 2','Pause Menu','Quit from game']
else:
    items = ['Play','Settings','Credits','Controls','Quit from game']

selected_section = 0

# Section colors
BLUE = (91, 207, 252)
DARK_BLUE = (38, 109, 135)

# Character position
character_x = 400
character_y = 300
character_speed = 5

# Scene switcher
current_scene = None
def switch_scene(scene):
    global current_scene
    current_scene = scene

def MainMenu():
    global running, selected_section
    running = True
    while running:
        
        # Quit Event
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()

            # Menu Controls
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        selected_section -= 1
                    elif e.key == pygame.K_DOWN:
                        selected_section += 1
                    elif e.key in [pygame.K_RETURN, pygame.K_SPACE]:
             # Menu tabs
                        if items[selected_section] == 'Quit from game': running = False, pygame.quit(), exit()
                        if items[selected_section] == 'Credits': credits_sign()
                        if items[selected_section] == 'Level select': running = False, Level_Select()
                        if items[selected_section] == 'Level 1': running = False, Level_1()
                        if items[selected_section] == 'Play': running = False, Level_1()
                        if items[selected_section] == 'Pause Menu': running = False, PauseMenu()

                    selected_section = selected_section % len(items)

       # 'Q' Key to quit
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_q:
                    running = False
                    pygame.quit()
                    exit()

        # Render images
            window.blit(bg,(-200, -0))
            window.blit(shirLogo,(822, -3))
            window.blit(build_info_text, (0,30))
            if DISTRIBUTE_TEXT == 1:
                window.blit(distribute_text, (0,0))
            window.blit(help_text, (0,60))
            window.blit(boosty_text, (0,590))
            window.blit(boosty_logo, (0,620))
            window.blit(youtube_logo, (120,590))
            window.blit(github_logo, (265,620))
            window.blit(gamejolt_logo, (385,620))
            window.blit(youtube_text, (120,590))
            window.blit(github_text, (265,590))
            window.blit(gamejolt_text, (380,590))

            # Credits Func       
            def credits_sign():
                window.blit(credits_sign_img,(300,100))
                window.blit(credits_title,(500,130))
                window.blit(credits_koirdev,(350,200))
                window.blit(credits_venux,(350,300))
                window.blit(credits_JBoT,(350,400))
                window.blit(credits_motver,(350,500))
                pygame.display.flip()           

        # Render Menu
            for i in range(len(items)):
                if i == selected_section:
                    menu_text = menu_font.render(items[i],0, BLUE)
                else:
                    menu_text = menu_font.render(items[i],0, DARK_BLUE)
                menu_text_rect = menu_text.get_rect(center = (WIDTH // 1.25, 250+ 50 * i))
                window.blit(menu_text, menu_text_rect)

        # Splashes
            if SPLASHES == 1:    
                window.blit(splash_text, (450,0)) 

        # Debug Func
            if DEBUG_MODE == 1:
                if FULLSCREEN == 1:
                    window.blit(fullscreen_text,(0,90))
                if RESIZABLE_WINDOW == 1:
                    window.blit(resizable_text, (0,90))
                if HARDWARE_RENDER == 1:
                    window.blit(hardware_render_text, (0,90))
                if DEFAULT_WINDOW == 1:
                    window.blit(default_window_text, (0,90))


        # Update screen
            pygame.display.update()
            clock.tick(FPS)

        # Show FPS on Console
            if DEBUG_MODE == 1:
                print(clock.get_fps())

            # Making Screenshot
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_7:
                    print("Saving...")
                    screen_shot()
                    print("Saved in screenshots/scrsht1.png")


def Level_1():
    global running, character_y, character_x, character_speed, LEVEL
    while running:

       # Quit Event
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

        # 'Q' Key to quit
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_q:
                    running = False
                    pygame.quit()
                    exit()
        # 'P' Key to pause
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_p:
                    PauseMenu()
                    running = False

                    
        # Player Controls
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_LSHIFT]:
            character_speed = 10
        else:
            character_speed = 5

        if keys[pygame.K_LEFT]:
            character_x -= character_speed

        if keys[pygame.K_RIGHT]:
            character_x += character_speed
       
        # Volume off
            if e.type == pygame.KEYUP:
                    if e.key == pygame.K_F1:
                        pygame.mixer.music.set_volume(0)
        # Volume on
            if e.type == pygame.KEYUP:
                    if e.key == pygame.K_F2:
                        pygame.mixer.music.set_volume(1)

        # Render images           
        window.fill((82, 212, 255))
        window.blit(build_info_text, (0,0))
        window.blit(door1, (1000,100))
        window.blit(character_img,(character_x, character_y))
        window.blit(grass_img, (-100,500))

        # Update screen
        pygame.display.update()
        clock.tick(FPS)

        # Show FPS on Console
        if DEBUG_MODE == 1:
            print(clock.get_fps())


def PauseMenu():
    global running, LEVEL
    while running:
       
       # Quit Event
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

        # 'P' Key to contiune
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_p:
                    Level_1()
                    running = False

         # 'Backspace' Key back to the main menu
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_BACKSPACE:
                    switch_scene(MainMenu)
                    running = False                   
                    
        # Render images
        window.fill((0, 0, 0))
        window.blit(pause_title_text,(550,250))
        window.blit(pause_tips_text1,(500,350))
        window.blit(pause_tips_text2,(350,400))
 
        # Update screen
        pygame.display.update()
        clock.tick(FPS)

        # Show FPS on Console
        if DEBUG_MODE == 1:
            print(clock.get_fps())

# Switch scene
switch_scene(MainMenu)
while current_scene is not None:
    current_scene()

