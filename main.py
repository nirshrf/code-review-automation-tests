import pygame


def main():
    pygame.init()
    logo = pygame.image.load("coffee-icon.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    screen = pygame.display.set_mode((500, 500))
    running = True
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

if __name__=="__main__":
    # call the main function
    main()