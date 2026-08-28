#imports
import pygame
import os
from settings import * 

#load map frames
def load_map_frames(map_num, no_of_frames, extension, for_menu):
    map_frames = []
    map_folder = os.path.join(BASE_DIR, "assets", "maps", map_num)
    for i in range(no_of_frames):
        frame_num = "frame" + str(i) + extension
        frame = pygame.image.load(os.path.join(map_folder, frame_num)).convert_alpha()
        if not for_menu:
            frame = pygame.transform.scale(frame, (GAME_WIDTH, GAME_HEIGHT))
        else:
            frame = pygame.transform.scale(frame, (map_menu_width, map_menu_height))
        map_frames.append(frame)

    return map_frames

#allow map animation to update
class Map:
    def __init__(self, map_num, no_of_frames, extension, cooldown, for_menu, pos):
        self.map_frames = load_map_frames(map_num, no_of_frames, extension, for_menu)
        self.current_frame = 0
        self.animation_cooldown = cooldown
        self.last_update = pygame.time.get_ticks()
        self.pos = pos

    def update(self):
        if pygame.time.get_ticks() - self.last_update > self.animation_cooldown:
            self.last_update = pygame.time.get_ticks()
            self.current_frame += 1
            if self.current_frame >= len(self.map_frames):
                self.current_frame = 0

        game_surface.blit(self.map_frames[self.current_frame], self.pos)

#setting up the 4 maps
map1 = Map("map1", 12, ".gif", 100, False, (0, 0))
map2 = Map("map2", 10, ".gif", 87, False, (0, 0))
map3 = Map("map3", 143, ".png", 65, False, (0, 0))
map4 = Map("map4", 42, ".png", 100, False, (0, 0))

map1_menu = Map("map1", 12, ".gif", 100, True, map_1_menu_pos)
map2_menu = Map("map2", 10, ".gif", 87, True, map_2_menu_pos)
map3_menu = Map("map3", 143, ".png", 65, True, map_3_menu_pos)
map4_menu = Map("map4", 42, ".png", 100, True, map_4_menu_pos)