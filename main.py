#imports
import pygame
import os
from settings import *
from maps import *
from sprites import *

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

    screen.fill((0, 0, 0))
    screen.blit(scaled_surface, (x_offset, y_offset))

#clock setup
clock = pygame.time.Clock()
FPS = 60

#define essential game settings
running = True
is_fullscreen = False

#main game loop
while running:

    #set up delta time
    dt = clock.tick(FPS) / 1000

    #check for events
    for event in pygame.event.get():

        #closing game
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

    #display map
    game_surface.blit(map1, (0, 0))

    #update display
    scale_game()
    pygame.display.update()

#exit pygame
pygame.quit()