#imports
import pygame
import os
from settings import * 

#load map frames
def load_map_frames(map_num, no_of_frames):
    map_frames = []
    map_folder = os.path.join(BASE_DIR, "assets", "maps", map_num)
    for i in range(no_of_frames):
        frame_num = "frame" + str(i) + ".gif"
        frame = pygame.image.load(os.path.join(map_folder, frame_num)).convert_alpha()
        frame = pygame.transform.scale(frame, (GAME_WIDTH, GAME_HEIGHT))
        map_frames.append(frame)

    return map_frames

#allow map animation to update
class Map:
    def __init__(self, map_num, no_of_frames):
        self.map_frames = load_map_frames(map_num, no_of_frames)
        self.current_frame = 0
        self.animation_cooldown = 100
        self.last_update = pygame.time.get_ticks()   

    def update(self):
        if pygame.time.get_ticks() - self.last_update > self.animation_cooldown:
            self.last_update = pygame.time.get_ticks()
            self.current_frame += 1
            if self.current_frame >= len(self.map_frames):
                self.current_frame = 0
                
        game_surface.blit(self.map_frames[self.current_frame], (0, 0))