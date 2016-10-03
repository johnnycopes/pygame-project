import pygame
from random import randint

class Monster(object):
    def __init__(self):
        self.x = 140
        self.y = 115
        self.x_speed = 4
        self.y_speed = 0
        self.width = 30
        self.height = 32
        self.image = pygame.image.load('images/monster.png').convert_alpha()

    def move(self, width, height):
        self.x += self.x_speed
        self.y += self.y_speed

        if self.x + self.x_speed > width - self.width:
            self.x = 0
        if self.x + self.x_speed < 0:
            self.x = width - self.width
        if self.y + self.y_speed > height - self.height:
            self.y = 0
        if self.y + self.y_speed < 0:
            self.y = height - self.height

    def change_direction(self):
        self.x_speed = 0
        self.y_speed = 0

        # move in a random direction
        direction = randint(1, 4)
        if direction == 1:
            self.x_speed = 4
        elif direction == 2:
            self.x_speed = -4
        elif direction == 3:
            self.y_speed = 4
        else:
            self.y_speed = -4


def main():
    # declare the size of the canvas
    width = 512
    height = 480
    tree_width = 25
    tree_height = 30

    # hero/monster position and speeds
    hero_x = 240
    hero_y = 215
    hero_x_speed = 0
    hero_y_speed = 0
    hero_width = 32
    hero_height = 32


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
    hero = pygame.image.load('images/hero.png').convert_alpha()
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
                    hero_x_speed = 3
                if event.key == pygame.K_LEFT:
                    hero_x_speed = -3
                if event.key == pygame.K_DOWN:
                    hero_y_speed = 3
                if event.key == pygame.K_UP:
                    hero_y_speed = -3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    hero_x_speed = 0
                if event.key == pygame.K_LEFT:
                    hero_x_speed = 0
                if event.key == pygame.K_DOWN:
                    hero_y_speed = 0
                if event.key == pygame.K_UP:
                    hero_y_speed = 0

            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True


        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################

        monster.move(width, height)
        if loop_counter > 120:
            monster.change_direction()
            loop_counter = 0


        if hero_x + hero_x_speed > width - hero_width - tree_width:
            hero_x_speed = 0
        if hero_x + hero_x_speed < 0 + tree_width:
            hero_x_speed = 0
        if hero_y + hero_y_speed > height - hero_height - tree_height:
            hero_y_speed = 0
        if hero_y + hero_y_speed < 0 + tree_height:
            hero_y_speed = 0


        hero_x += hero_x_speed
        hero_y += hero_y_speed


        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        screen.blit(bg_img, (0, 0))
        screen.blit(hero, (hero_x, hero_y))
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
