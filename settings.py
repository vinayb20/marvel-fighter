#imports
import pygame
import os

#initialise pygame
pygame.init()

#screen setup
GAME_WIDTH = 1280
GAME_HEIGHT = 720
game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("marvel-fighter")

#base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


