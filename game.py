import pygame
import os

# set up
WIDTH = 800
HEIGHT = 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Game")

MARIO_WIDTH = 55
MARIO_HEIGHT = 40


# put mario on screen
MARIO_IMAGE = pygame.image.load(os.path.join('mario.png'))
MARIO = pygame.transform.rotate(pygame.transform.scale(MARIO_IMAGE, (MARIO_WIDTH, MARIO_HEIGHT)),0)


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WINDOW.fill((0,51,255))
        WINDOW.blit(MARIO, (100,320))
        pygame.display.update()

    pygame.quit()

main()