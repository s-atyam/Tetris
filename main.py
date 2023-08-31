import pygame
import sys

# initilise pygame
pygame.init()

# game colors
purple_shade_1 = (111, 36, 145)

# window screen (display surface)
screen = pygame.display.set_mode((300,600))

# set the title of window
pygame.display.set_caption("Tetris")

# clock object
clock = pygame.time.Clock()

while True:
    # all the vent handling in the game
    for event in pygame.event.get():
        # for quiting the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # drawing
    screen.fill(purple_shade_1)
    pygame.display.update()
    clock.tick(60) # all the code inside while loop will run 60 time per second
