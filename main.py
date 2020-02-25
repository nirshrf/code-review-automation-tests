import pygame


def main():
    cats_on_screen, counter = 0, 0
    pygame.init()
    logo = pygame.image.load("coffee-icon.png")
    cat_image = pygame.image.load("cat4.png")
    cat_image_dimension = 232, 193
    cat_image.set_colorkey((255, 255, 255))
    cat_image.set_alpha(255)
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    screen_width = 500
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((80, 160, 100), rect=None, special_flags=0)
    x_pos = 50
    y_pos = 50
    screen.blit(cat_image, (x_pos, y_pos))
    step_x = 10
    step_y = 10
    pygame.display.flip()
    # screen.blit(bgd_image, (0, 0))
    running = True
    while running:
        # event handling, gets all event from the event queue
        # check if the smiley is still on screen, if not change direction
        # update the position of the smiley
        counter += 1
        if counter == 750:
            counter = 0
            cats_on_screen += 1
            cat_image.set_alpha(51 * cats_on_screen)
            if x_pos > screen_width - cat_image_dimension[0] or x_pos < 0:
                step_x = -step_x
            if y_pos > screen_height - cat_image_dimension[1] or y_pos < 0:
                step_y = -step_y
            x_pos += step_x  # move it to the right
            y_pos += step_y  # move it down
            if cats_on_screen == 5:
                cats_on_screen = 0
                screen.fill((80, 160, 100), rect=None, special_flags=0)
            screen.blit(cat_image, (x_pos, y_pos))
            pygame.display.flip()
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


if __name__ == "__main__":
    # call the main function
    main()
