#imports
import pygame
import os
import settings
from settings import *
from maps import *
from sprites import *
from gui import * 

#fullscreen function
def scale_game():
    screen_width, screen_height = screen.get_size()

    scale_x = screen_width / GAME_WIDTH
    scale_y = screen_height / GAME_HEIGHT
    scale = min(scale_x, scale_y)

    scaled_width = int(GAME_WIDTH * scale)
    scaled_height = int(GAME_HEIGHT * scale)
    scaled_surface = pygame.transform.scale(game_surface, (scaled_width, scaled_height))

    x_offset = (screen_width - scaled_width) // 2
    y_offset = (screen_height - scaled_height) // 2

    settings.scale = scale
    settings.x_offset = x_offset
    settings.y_offset = y_offset

    screen.fill((0, 0, 0))
    screen.blit(scaled_surface, (x_offset, y_offset))

#clock setup
clock = pygame.time.Clock()
FPS = 60

#define essential game settings
running = True
is_fullscreen = False
game_state = "menu"

#main game loop
while running:

    #set up delta time
    dt = clock.tick(FPS) / 1000

    #check for events
    events = pygame.event.get()
    for event in events:

        #closing game if x
        if event.type == pygame.QUIT:
            running = False

        #entering full screen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                is_fullscreen = not is_fullscreen
                if is_fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT), pygame.RESIZABLE)

    #game states
    if game_state == "menu":
        map4.update()
        menu_action = main_menu(events)
        if menu_action == "quit":
            running = False
        elif menu_action == "play":
            game_state = "map_select"

    elif game_state == "map_select":
        map4.update()
        menu_action = maps(events)
        if menu_action is not None:
            game_state = menu_action

    elif game_state == "map1" or game_state == "map2" or game_state == "map3" or game_state == "map4":
        if game_state == "map1":
            map1.update()
        elif game_state == "map2":
            map2.update()
        elif game_state == "map3":
            map3.update()
        elif game_state == "map4":
            map4.update()

        menu_action = hero_select(events)
        if menu_action is not None:
            game_state = menu_action
    
    elif game_state == "game":
        if settings.map_selection == "map1":
            map1.update()
        if settings.map_selection == "map2":
            map2.update()
        if settings.map_selection == "map3":
            map3.update()
        if settings.map_selection == "map4":
            map4.update()

    #update display
    scale_game()
    pygame.display.update()

#exit pygame
pygame.quit()