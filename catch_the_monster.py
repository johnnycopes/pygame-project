import pygame
from random import randint

class Monster(object):
    def __init__(self):
        self.x = 140
        self.y = 115
        self.x_speed = 3
        self.y_speed = 0
        self.width = 32
        self.height = 30
        self.image = pygame.image.load('images/monster.png').convert_alpha()


def main():
    # declare the size of the canvas
    width = 512
    height = 480

    # hero/monster position and speeds
    hero_x = 240
    hero_y = 215


    # initialize the pygame framework
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################


    bg_img = pygame.image.load('images/background.png').convert_alpha()
    hero_img = pygame.image.load('images/hero.png').convert_alpha()
    monster = Monster()

    # game loop
    stop_game = False
    loop_counter = 0
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################

        monster.x += monster.x_speed
        monster.y += monster.y_speed

        if monster.x + monster.x_speed > width - monster.width:
            monster.x = 0
        if monster.x + monster.x_speed < 0:
            monster.x = width - monster.width
        if monster.y + monster.y_speed > height - monster.height:
            monster.y = 0
        if monster.y + monster.y_speed < 0:
            monster.y = height - monster.height


        if loop_counter > 120:

            monster.x_speed = 0
            monster.y_speed = 0

            # make the monster move in a random direction
            direction = randint(1, 4)
            if direction == 1:
                monster.x_speed = 3
            elif direction == 2:
                monster.x_speed = -3
            elif direction == 3:
                monster.y_speed = 3
            else:
                monster.y_speed = -3

            loop_counter = 0



        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        screen.blit(bg_img, (0, 0))
        screen.blit(hero_img, (hero_x, hero_y))
        screen.blit(monster.image, (monster.x, monster.y))

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

        # increase loop_counter
        loop_counter += 1

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
