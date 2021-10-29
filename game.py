import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import entities

# set up
WIDTH = 800
HEIGHT = 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Game")

# set up background
BACKGROUND_WIDTH = 800
BACKGROUND_HEIGHT = 400
BACKGROUND = pygame.image.load(os.path.join('bg.png'))
BACKGROUNDIMAGE = pygame.transform.rotate(pygame.transform.scale(BACKGROUND, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT)),0)

# set up pipes
OBSTACLE1 = pygame.image.load(os.path.join('pipe1.png'))
PIPE = pygame.transform.rotate(pygame.transform.scale(OBSTACLE1, (60, 80)),0)
PIPETWO = pygame.transform.rotate(pygame.transform.scale(OBSTACLE1, (60, 100)),0)

# main game loop
# draws entities, background, and objects onto the screen
def main():
    run = True
    bgx=0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WINDOW.blit(BACKGROUNDIMAGE, (bgx-WIDTH, 0))
        WINDOW.blit(BACKGROUNDIMAGE, (bgx,0))
        WINDOW.blit(BACKGROUNDIMAGE, (bgx+WIDTH, 0))
        WINDOW.blit(PIPE, (300,280))
        WINDOW.blit(PIPETWO, (500, 260))

        # update all entities
        entities.get_entity_list().update()
        # draw all sprites onto screen
        entities.get_entity_list().draw(WINDOW)

        # screen scrolling (commented out for now)
        #bgx = bgx - 1
        #if bgx <= -1*WIDTH:
        #   bgx = 0
        pygame.display.update()

    pygame.quit()

main()