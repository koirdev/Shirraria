from config import * 
from sound_loader import *
from graphics_loader import *
from text_loader import *
from openLinks import *
import pygame, sys, asyncio

print("WARNING: This game is cancelled, this build has many unfinished and buggy features! Play at your own risk! There will be no more updates")

# Checking init error
game_init = pygame.init()
if(game_init[1]>0):
    print("Game Init Failed")

# Window options
window = pygame.display.set_mode((WIDTH,HEIGHT))

# Window title and icon
pygame.display.set_caption("Shirraria")
icon = pygame.image.load('assets/images/icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# Menu Sections
items = ['Play','Settings','GitHub page','Open debug logs']

selected_section = 0

# Section colors
CYAN = (91, 207, 252)
DARK_CYAN = (38, 109, 135)

# Character position
character_x = 400
character_y = 300
character_speed = 5

async def MainMenu():
    global running, selected_section, shirLogo, CONTROLS, TestStage
    running = True
    while running:
            
        # Quit Event
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()


            # Menu Controls
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        selected_section -= 1
                        if SFX == 1:
                            clickSound.play()
                    elif e.key == pygame.K_DOWN:
                        selected_section += 1
                        if SFX == 1:
                            clickSound.play()
                    elif e.key in [pygame.K_RETURN, pygame.K_SPACE]:
                        if SFX == 1:
                            whooshSound.play()

            # Menu tabs
                        if items[selected_section] == 'Credits': pass
                        if items[selected_section] == 'Level select': running = False, Level_Select()
                        if items[selected_section] == 'Level 1': running = False, Level_1()
                        if items[selected_section] == 'Play': pass
                        if items[selected_section] == 'Open Log file': pass
                        if items[selected_section] == 'GitHub page': OpenGitHubLink()
                        if items[selected_section] == 'Open debug logs' : OpenDebugLinkLocal()


                    selected_section = selected_section % len(items)

        # 'Q' Key to quit
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_q:
                    sys.exit()

        # Render images
            window.blit(bg,(0, -0))
            window.blit(shirLogo,(WIDTH // 1.4,HEIGHT // 65))
            window.blit(build_info_text, (0,30))
            window.blit(build_info_text, (0,30))
            if WARNING_TEXT == 1:
                window.blit(warning_text, (0,0))
            window.blit(help_text, (0,60))


        # Render Menu
            for i in range(len(items)):
                if i == selected_section:
                    menu_text = menu_font.render(items[i],0, CYAN)
                else:
                    menu_text = menu_font.render(items[i],0, DARK_CYAN)
                menu_text_rect = menu_text.get_rect(center = (WIDTH // 1.21, 250+ 50 * i))
                window.blit(menu_text, menu_text_rect)

        # Splashes
            if SPLASHES == 1:
                window.blit(splash_text, (WIDTH // 2.7, HEIGHT // 170)) 

        # Update screen
            pygame.display.update()
            clock.tick(FPS)
            await asyncio.sleep(0)


asyncio.run(MainMenu())






    


