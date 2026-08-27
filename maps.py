import pygame
import os
from settings import * 

#map1 setup
map1 = pygame.image.load(os.path.join(BASE_DIR, "assets", "maps", "map1.gif")).convert_alpha()
map1 = pygame.transform.scale(map1, (GAME_WIDTH, GAME_HEIGHT))