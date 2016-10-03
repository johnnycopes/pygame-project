import pygame
from random import randint


class Ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5
        self.radius = randint(20, 100)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x + self.radius > width:
            self.speed_x = -5
        if self.y + self.radius > height:
            self.speed_y = -5
        if self.x - self.radius < 0:
            self.speed_x = 5
        if self.y - self.radius < 0:
            self.speed_y = 5

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


def main():
    # declare the size of the canvas
    width = 600
    height = 600
    bg_color = (randint(0, 255), randint(0, 255), randint(0, 255))


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
    ball_list = [
        Ball(0, 400),
        Ball(40, 360),
        Ball(80, 320),
        Ball(120, 280),
        Ball(160, 240),
        Ball(200, 200),
        Ball(240, 160),
        Ball(280, 120),
        Ball(320, 80),
        Ball(360, 40),
        Ball(400, 0)
    ]

    # game loop
    stop_game = False
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
        for ball in ball_list:
            ball.update(width, height)

        # fill background color
        screen.fill(bg_color)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        for ball in ball_list:
            ball.render(screen)

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
