import pygame

def main():
    # declare the size of the canvas
    width = 515
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
    hero_img = pygame.image.load('images/hero.png').convert_alpha()
    monster_img = pygame.image.load('images/monster.png').convert_alpha()

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

        # fill background color
        # screen.fill(bg_img)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        screen.blit(bg_img, (0, 0))
        screen.blit(hero_img, (240, 215))
        screen.blit(monster_img, (140, 115))

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
