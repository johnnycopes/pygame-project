import pygame
import math
from random import randint

def distance(thing1, thing2):
    return math.sqrt((thing1.x - thing2.x) ** 2 + (thing1.y - thing2.y) ** 2)

class Character(object):
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Hero(Character):
    def __init__(self):
        self.x = 240
        self.y = 215
        self.x_speed = 0
        self.y_speed = 0
        self.speed = 4
        self.size = 32
        self.image = pygame.image.load('images/hero.png')

    def collides(self, enemy):
        return distance(self, enemy) < 32

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

    def process_event(self, event):
        # Keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.x_speed = self.speed
            if event.key == pygame.K_LEFT:
                self.x_speed = -self.speed
            if event.key == pygame.K_DOWN:
                self.y_speed = self.speed
            if event.key == pygame.K_UP:
                self.y_speed = -self.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.x_speed = 0
            if event.key == pygame.K_LEFT:
                self.x_speed = 0
            if event.key == pygame.K_DOWN:
                self.y_speed = 0
            if event.key == pygame.K_UP:
                self.y_speed = 0


class Goblin(Character):
    def __init__(self):
        self.x = 340
        self.y = 115
        self.x_speed = -3
        self.y_speed = 0
        self.speed = 3
        self.size = 32
        self.image = pygame.image.load('images/goblin.png')
        self.timer = 0

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

        self.check_timer()

    def check_timer(self):
        self.timer += 1
        if self.timer > 100:
            self.change_direction()
            self.timer = 0

    def change_direction(self):
        # move in a random direction
        direction = randint(1, 4)
        diagonal = randint(-self.speed, self.speed)
        if direction == 1:
            self.x_speed = self.speed
            self.y_speed = diagonal
        elif direction == 2:
            self.x_speed = -self.speed
            self.y_speed = diagonal
        elif direction == 3:
            self.y_speed = self.speed
            self.x_speed = diagonal
        else:
            self.y_speed = -self.speed
            self.x_speed = diagonal

    def respawn(self, width, height):
        self.x = randint(0, width)
        self.y = randint(0, height)


class Monster(Character):
    def __init__(self):
        self.x = 140
        self.y = 115
        self.x_speed = 4
        self.y_speed = 0
        self.speed = 5
        self.size = 32
        self.image = pygame.image.load('images/monster.png')
        self.timer = 0

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

        self.check_timer()

    def check_timer(self):
        self.timer += 1
        if self.timer > 120:
            self.change_direction()
            self.timer = 0

    def change_direction(self):
        # move in a random direction
        direction = randint(1, 4)
        diagonal = randint(-self.speed, self.speed)
        if direction == 1:
            self.x_speed = self.speed
            self.y_speed = diagonal
        elif direction == 2:
            self.x_speed = -self.speed
            self.y_speed = diagonal
        elif direction == 3:
            self.y_speed = self.speed
            self.x_speed = diagonal
        else:
            self.y_speed = -self.speed
            self.x_speed = diagonal

    def respawn(self, width, height):
        self.x = randint(0, width)
        self.y = randint(0, height)


def main():
    # set game_over to False until hero collides with monster
    game_over = False

    # set game_won / game_lost variables
    win = False
    lose = False

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
    pygame.mixer.init()
    bg_img = pygame.image.load('images/background.png')
    win_sound = pygame.mixer.Sound('sounds/win.wav')
    lose_sound = pygame.mixer.Sound('sounds/lose.wav')

    hero = Hero()
    monster = Monster()
    goblin = Goblin()

    # game loop
    stop_game = False
    loop_counter = 0
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            hero.process_event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_over = False
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True


        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################

        if not game_over:
            hero.move(width, height)
            monster.move(width, height)
            goblin.move(width, height)
            if hero.collides(monster):
                game_over = True
                win_sound.play()
                monster.respawn(width, height)
                goblin.respawn(width, height)
            elif hero.collides(goblin):
                game_over = True
                lose_sound.play()
                monster.respawn(width, height)
                goblin.respawn(width, height)



        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        screen.blit(bg_img, (0, 0))

        hero.render(screen)
        if game_over:
            font = pygame.font.Font(None, 40)
            text = font.render("Hit ENTER to play again!", True, (0, 0, 0))
            screen.blit(text, (80, 250))
        else:
            monster.render(screen)
            goblin.render(screen)

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
