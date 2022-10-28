
import pygame as py
# import level as lvl
from OtherCode import sprite_loading as sl


class Dir:
    NONE = 0
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


screen_size = (1920, 1080)
black = (0, 0, 0)
vel = 3                                                         # vel sets the speed of the character
display = py.display.set_mode(screen_size)
sprites = sl.load_all()


def main():
    py.init()
    curr_dir = []
    x = 300
    y = 300

    while True:
        py.time.delay(10)
        display.fill(black)
        display.blit(sprites[sl.Sprite.PLAY.value], (x, y))
        py.display.flip()

# ----------------------------------------------------- movement ----------------------------------------------------- #

        for move in curr_dir:
            match move:
                case Dir.NONE:
                    pass

                case Dir.UP:
                    y -= vel

                case Dir.DOWN:
                    y += vel

                case Dir.LEFT:
                    x -= vel

                case Dir.RIGHT:
                    x += vel

        for event in py.event.get():
            if event.type == py.KEYDOWN:
                match event.key:
                    case py.K_w:
                        curr_dir.append(Dir.UP)

                    case py.K_a:
                        curr_dir.append(Dir.LEFT)

                    case py.K_s:
                        curr_dir.append(Dir.DOWN)

                    case py.K_d:
                        curr_dir.append(Dir.RIGHT)

            elif event.type == py.KEYUP:
                match event.key:
                    case py.K_w:
                        curr_dir.remove(Dir.UP)
                    case py.K_a:
                        curr_dir.remove(Dir.LEFT)

                    case py.K_s:
                        curr_dir.remove(Dir.DOWN)

                    case py.K_d:
                        curr_dir.remove(Dir.RIGHT)

# ------------------------------------------------- end of movement -------------------------------------------------- #

            # here we check for program close
            if event.type == py.QUIT:
                return


# ----------------------------------------------------- main --------------------------------------------------------- #


main()
