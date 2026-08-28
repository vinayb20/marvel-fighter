#imports
import pygame
import settings
from settings import *
from maps import *

#load sprite menu selection images
spiderman_menu = pygame.image.load(os.path.join(BASE_DIR, "assets", "sprites", "images", "spiderman.jpeg"))
spiderman_menu = pygame.transform.scale(spiderman_menu, (sprite_menu_width, sprite_menu_height))

ironman_menu = pygame.image.load(os.path.join(BASE_DIR, "assets", "sprites", "images", "ironman.jpeg"))
ironman_menu = pygame.transform.scale(ironman_menu, (sprite_menu_width, sprite_menu_height))

wolverine_menu = pygame.image.load(os.path.join(BASE_DIR, "assets", "sprites", "images", "wolverine.jpeg"))
wolverine_menu = pygame.transform.scale(wolverine_menu, (sprite_menu_width, sprite_menu_height))

captainAmerica_menu = pygame.image.load(os.path.join(BASE_DIR, "assets", "sprites", "images", "captainamerica.jpeg"))
captainAmerica_menu = pygame.transform.scale(captainAmerica_menu, (sprite_menu_width, sprite_menu_height))

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

def draw_map_button(x, y, padding=2):
    button_rect = pygame.Rect(x - padding, y - padding, map_menu_width + (padding*2), map_menu_height + (padding*2))
    
    mouse_pos = get_game_mouse_pos()
    if button_rect.collidepoint(mouse_pos):
        drawing_box_col = RED
    else:
        drawing_box_col = WHITE

    pygame.draw.rect(game_surface, drawing_box_col, button_rect, 5)
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

def maps(events):
    draw_text("MAIN MENU", pressStart2P_font, YELLOW, 280, 60)
    draw_text("SELECT A MAP", pressStart2P_font_for_map_menu, WHITE, 450, 152)
    full_screen_rect = draw_rect(False, "PRESS F TO TOGGLE FULLSCREEN", blox2_font, BLACK, BLUE, 920, 660, 5)

    map1_menu.update()
    map1_button = draw_map_button(map_1_menu_pos[0], map_1_menu_pos[1])

    map2_menu.update()
    map2_button = draw_map_button(map_2_menu_pos[0], map_2_menu_pos[1])

    map3_menu.update()
    map3_button = draw_map_button(map_3_menu_pos[0], map_3_menu_pos[1])

    map4_menu.update()
    map4_button = draw_map_button(map_4_menu_pos[0], map_4_menu_pos[1])

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = get_game_mouse_pos()
            if map1_button.collidepoint(mouse_pos):
                return "map1"
            elif map2_button.collidepoint(mouse_pos):
                return "map2"
            elif map3_button.collidepoint(mouse_pos):
                return "map3"
            elif map4_button.collidepoint(mouse_pos):
                return "map4"

    return None

def draw_sprite_selection_button(x, y, selected, padding=2):
    button_rect = pygame.Rect(x - padding, y - padding, map_menu_width + (padding*2), map_menu_height + (padding*2))

    drawing_box_col = WHITE

    if not selected and settings.selected_count < 2:   
        mouse_pos = get_game_mouse_pos()
        if button_rect.collidepoint(mouse_pos):
            drawing_box_col = RED
        else:
            drawing_box_col = WHITE

    if selected:
        drawing_box_col = GREEN

    pygame.draw.rect(game_surface, drawing_box_col, button_rect, 5)
    return button_rect

def hero_select(events):
    draw_text("MAIN MENU", pressStart2P_font, YELLOW, 280, 60)
    draw_text("SELECT A HERO", pressStart2P_font_for_map_menu, WHITE, 450, 152)

    game_surface.blit(spiderman_menu, sprite_1_menu_pos)
    spiderman_button = draw_sprite_selection_button(sprite_1_menu_pos[0], sprite_1_menu_pos[1], settings.spiderman_selected)

    game_surface.blit(ironman_menu, sprite_2_menu_pos)
    ironman_button = draw_sprite_selection_button(sprite_2_menu_pos[0], sprite_2_menu_pos[1], settings.ironman_selected)

    game_surface.blit(captainAmerica_menu, sprite_3_menu_pos)
    captainAmerica_button = draw_sprite_selection_button(sprite_3_menu_pos[0], sprite_3_menu_pos[1], settings.captainAmerica_selected)

    game_surface.blit(wolverine_menu, sprite_4_menu_pos)
    wolverine_button = draw_sprite_selection_button(sprite_4_menu_pos[0], sprite_4_menu_pos[1], settings.wolverine_selected)

    if settings.selected_count < 2:
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = get_game_mouse_pos()
                if spiderman_button.collidepoint(mouse_pos):
                    settings.spiderman_selected = True
                    settings.selected_count += 1
                elif ironman_button.collidepoint(mouse_pos):
                    settings.ironman_selected = True
                    settings.selected_count += 1
                elif captainAmerica_button.collidepoint(mouse_pos):
                    settings.captainAmerica_selected = True
                    settings.selected_count += 1
                elif wolverine_button.collidepoint(mouse_pos):
                    settings.wolverine_selected = True
                    settings.selected_count += 1