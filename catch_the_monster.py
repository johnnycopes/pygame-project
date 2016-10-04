import pygame
import math
from random import randint


class Hero(object):
    def __init__(self):
        self.x = 240
        self.y = 215
        self.x_speed = 0
        self.y_speed = 0
        self.size = 32
        self.image = pygame.image.load('images/hero.png').convert_alpha()

    def move(self, width, height):
        self.x += self.x_speed
        self.y += self.y_speed

        # 25/30 are the width/height values of the trees
        if self.x + self.x_speed > width - self.size - 25:
            self.x = width - self.size - 25
        if self.x + self.x_speed < 0 + 25:
            self.x = 0 + 25
        if self.y + self.y_speed > height - self.size - 30:
            self.y = height - self.size - 30
        if self.y + self.y_speed < 0 + 30:
            self.y = 0 + 30


class Monster(object):
    def __init__(self):
        self.x = 140
        self.y = 115
        self.x_speed = 4
        self.y_speed = 0
        self.size = 32
        self.dead = False
        self.image = pygame.image.load('images/monster.png').convert_alpha()

    def move(self, width, height):
        self.x += self.x_speed
        self.y += self.y_speed

        if self.x + self.x_speed > width - self.size:
            self.x = 0
        if self.x + self.x_speed < 0:
            self.x = width - self.size
        if self.y + self.y_speed > height - self.size:
            self.y = 0
        if self.y + self.y_speed < 0:
            self.y = height - self.size

    def change_direction(self):
        self.x_speed = 0
        self.y_speed = 0

        # move in a random direction
        direction = randint(1, 4)
        diagonal = randint(-4, 4)
        if direction == 1:
            self.x_speed = 4
            self.y_speed = diagonal
        elif direction == 2:
            self.x_speed = -4
            self.y_speed = diagonal
        elif direction == 3:
            self.y_speed = 4
            self.x_speed = diagonal
        else:
            self.y_speed = -4
            self.x_speed = diagonal


def main():
    # declare the size of the canvas
    width = 512
    height = 480

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
    hero = Hero()
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

            # Keyboard events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    hero.x_speed = 3
                if event.key == pygame.K_LEFT:
                    hero.x_speed = -3
                if event.key == pygame.K_DOWN:
                    hero.y_speed = 3
                if event.key == pygame.K_UP:
                    hero.y_speed = -3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    hero.x_speed = 0
                if event.key == pygame.K_LEFT:
                    hero.x_speed = 0
                if event.key == pygame.K_DOWN:
                    hero.y_speed = 0
                if event.key == pygame.K_UP:
                    hero.y_speed = 0

            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True


        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################

        hero.move(width, height)
        monster.move(width, height)
        if loop_counter > 120:
            monster.change_direction()
            loop_counter = 0



        # Collison check
        if math.sqrt((hero.x - monster.x) ** 2 + (hero.y - monster.y) ** 2) < 32.0:
            monster.dead = True
            pygame.mixer.init()
            pygame.mixer.music.load('sounds/win.wav')


        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        screen.blit(bg_img, (0, 0))
        screen.blit(hero.image, (hero.x, hero.y))
        if not monster.dead:
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
