import pygame
import math

file_to_int = {"a": 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8}
int_to_file = {1 : "a", 2 : "b", 3 : "c", 4 : "d", 5 : "e", 6 : "f", 7 : "g", 8 : "h"}

file_change = lambda file_num: 287 + file_num * 75
rank_change = lambda rank: 610 - (rank - 1) * 75

def pos_to_cell(mouse_pos) -> tuple[int, int]:
    x_pos, y_pos = mouse_pos

    file_num: int = math.floor((x_pos - 267) // 75)
    rank: int = math.floor((590 - y_pos) // 75) + 2

    return file_num, rank


def scale_image_uneven(img, factor_x, factor_y) -> pygame.transform:
    size = round(img.get_width() * factor_x), round(img.get_height() * factor_y)
    return pygame.transform.scale(img, size)

def scale_image_even(img, factor) -> pygame.transform:
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)
