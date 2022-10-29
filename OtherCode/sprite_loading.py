import pygame as py
from enum import Enum

# 1920 x 1080  = 64 x 36


# ------------------------------------------------- load the files --------------------------------------------------- #


def load_all():
    sprites = []
    play_img = py.image.load("D:/FH/3.Semester/Python/Code/GJuan/SpriteSheets_etc/temp_Play.png")
    player_sheet = py.image.load('D:/FH/3.Semester/Python/Code/GJuan/SpriteSheets_etc/PlayerModels.png')

    sprites.insert(0, play_img)
    sprites.insert(1, extract_ss(player_sheet))

    return sprites


# ------------------------------------------ extract from sprite-sheet ----------------------------------------------- #


def extract_ss(sprite_sheet):
    back = []
    for i in range(1, 100):
        for o in range(1, 100):
            sprite_sheet.set_clip(py.Rect((o - 1) * 30 + o, (i - 1) * 30 + i, 30, 30))
            back.append(sprite_sheet.subsurface(sprite_sheet.get_clip()))

    return back

# ----------------------------------------- enums to access sprites easy --------------------------------------------- #


class Sprite(Enum):
    PLAY = 0
    PLAYER = 1
