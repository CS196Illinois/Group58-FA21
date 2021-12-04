import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import map
import window
import camera

win = window.WINDOW
camera = camera.Camera()
camera.update()

# set up background
BACKGROUND_WIDTH = window.WIDTH
BACKGROUND_HEIGHT = window.HEIGHT
BACKGROUND = pygame.image.load(os.path.join('images/bg2.png'))
BACKGROUNDIMAGE = pygame.transform.rotate(pygame.transform.scale(BACKGROUND, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT)),0)

VICT_WIDTH = 1000
VICT_HEIGHT = 300
VICT_IMAGE_LOAD = pygame.image.load(os.path.join('images/victory_royale.png'))
VICT_IMAGE = pygame.transform.rotate(pygame.transform.scale(VICT_IMAGE_LOAD,(VICT_WIDTH, VICT_HEIGHT)),0)

# main game loop
# draws entities, background, and objects onto the screen
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.blit(BACKGROUNDIMAGE, (0, 0))
        # update all entities
        map.ENTITY_LIST.update(map.OBJECT_LIST, map.FLAG)
        # draw objects onto screen
        camera.update()
        map.OBJECT_LIST.draw(win)
        # draw all sprites onto screen
        map.ENTITY_LIST.draw(win)
        pygame.display.update()

    pygame.quit()

def game_over():
    pass

def game_won():
    run = False
    win.blit(VICT_IMAGE_LOAD)

main()