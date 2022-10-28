import pygame as py
from enum import Enum

# 1920 x 1080  = 64 x 36


# ------------------------------------------------- load the files --------------------------------------------------- #


def load_all():
    sprites = []
    play_img = py.image.load("../SpriteSheets_etc/temp_Play.png")

    sprites.insert(0, play_img)

    return sprites


# ----------------------------------------- enums to access sprites easy --------------------------------------------- #


class Sprite(Enum):
    PLAY = 0
    P_Head_R = 1
