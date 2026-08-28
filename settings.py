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

#scaling settings
scale = 1 
x_offset = 0
y_offset = 0

#base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#fonts
pressStart2P_font = pygame.font.Font(os.path.join(BASE_DIR, "assets", "fonts", "PressStart2P-Regular.ttf"), 80)
pressStart2P_font_for_map_menu = pygame.font.Font(os.path.join(BASE_DIR, "assets", "fonts", "PressStart2P-Regular.ttf"), 30)
pressStart2P_font_for_input_menu = pygame.font.Font(os.path.join(BASE_DIR, "assets", "fonts", "PressStart2P-Regular.ttf"), 37)
publicPixel_font = pygame.font.Font(os.path.join(BASE_DIR, "assets", "fonts", "PublicPixel.ttf"), 50)
blox2_font = pygame.font.Font(os.path.join(BASE_DIR, "assets", "fonts", "blox2.ttf"), 25)

#colours
WHITE = (255, 255, 255)
DARKGREY = (40, 40, 40)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 120, 160)
GREEN = (0, 255, 0)

#map menu settings
map_menu_width, map_menu_height = 768/3, 480/3
map_1_menu_pos = (65, 200)
map_2_menu_pos = (365, 200)
map_3_menu_pos = (665, 200)
map_4_menu_pos = (965, 200)

map_selection = ""

#sprite selection menu settings
sprite_menu_width, sprite_menu_height = 768/3, 480/3
sprite_1_menu_pos = (65, 200)
sprite_2_menu_pos = (365, 200)
sprite_3_menu_pos = (665, 200)
sprite_4_menu_pos = (965, 200)

spiderman_selected = False
ironman_selected = False
captainAmerica_selected = False
wolverine_selected = False

selected_count = 0

p1 = ""
p2 = ""

#select input
game_input = ""