
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
max_vel = 7                                                         # max vel sets the max speed of the character
acc = 1
dacc = 0.5
display = py.display.set_mode(screen_size)
sprites = sl.load_all()


def main():
    py.init()
    curr_dir = []
    vel_x = 0                                                       # vel_X is the current speed on x-axis
    vel_y = 0                                                       # vel_y is the current speed on y-axis
    x = 300
    y = 300

    while True:
        py.time.delay(10)

        x += vel_x
        y += vel_y

        display.fill(black)
        display.blit(sprites[sl.Sprite.PLAY.value], (x, y))
        py.display.flip()

# ----------------------------------------------------- movement ----------------------------------------------------- #

        x_p = True
        y_p = True
        if vel_x < 0:
            x_p = False
        if vel_y < 0:
            y_p = False

        for move in curr_dir:
            match move:
                case Dir.UP:
                    if vel_y > - max_vel:
                        vel_y -= acc

                case Dir.DOWN:
                    if vel_y < max_vel:
                        vel_y += acc

                case Dir.LEFT:
                    if vel_x > - max_vel:
                        vel_x -= acc

                case Dir.RIGHT:
                    if vel_x < max_vel:
                        vel_x += acc

        if len(curr_dir) == 0:
            if vel_y < 0:
                vel_y += dacc

            elif vel_y > 0:
                vel_y -= dacc

            if vel_x < 0:
                vel_x += dacc

            elif vel_x > 0:
                vel_x -= dacc

        for event in py.event.get():
            if event.type == py.KEYDOWN:
                match event.key:
                    case py.K_w:
                        if y_p:
                            vel_y = 0
                        curr_dir.append(Dir.UP)

                    case py.K_a:
                        if x_p:
                            vel_x = 0
                        curr_dir.append(Dir.LEFT)

                    case py.K_s:
                        if not y_p:
                            vel_y = 0
                        curr_dir.append(Dir.DOWN)

                    case py.K_d:
                        if not x_p:
                            vel_x = 0
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
