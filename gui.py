import pygame
import settings
from settings import *

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    game_surface.blit(img, (x, y))

def get_game_mouse_pos():
    raw_x, raw_y = pygame.mouse.get_pos()
    adjusted_x = (raw_x - settings.x_offset) / settings.scale
    adjusted_y = (raw_y - settings.y_offset) / settings.scale
    return (adjusted_x, adjusted_y)

def draw_rect(button, text, font, text_col, box_col, x, y, padding):
    text_width, text_height = font.size(text)
    button_rect = pygame.Rect(x - padding, y - padding, text_width + (padding*2), text_height + (padding*2))

    if button:
        mouse_pos = get_game_mouse_pos()
        if button_rect.collidepoint(mouse_pos):
            drawing_box_col = RED
        else:
            drawing_box_col = DARKGREY
        pygame.draw.rect(game_surface, drawing_box_col, button_rect)
        pygame.draw.rect(game_surface, WHITE, button_rect, 3)
    else:
        pygame.draw.rect(game_surface, box_col, button_rect)
        pygame.draw.rect(game_surface, GREEN, button_rect, 3)
    
    draw_text(text, font, text_col, x, y)

    return button_rect
    
def main_menu(events):
    draw_text("MAIN MENU", pressStart2P_font, YELLOW, 280, 60)
    play_rect = draw_rect(True, "PLAY", publicPixel_font, WHITE, DARKGREY, 400, 200, 20)
    quit_rect = draw_rect(True, "QUIT", publicPixel_font, WHITE, DARKGREY, 700, 200, 20)
    full_screen_rect = draw_rect(False, "PRESS F TO TOGGLE FULLSCREEN", blox2_font, BLACK, BLUE, 920, 660, 5)

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = get_game_mouse_pos()
            if quit_rect.collidepoint(mouse_pos):
                return "quit"
            if play_rect.collidepoint(mouse_pos):
                return "play"

    return None