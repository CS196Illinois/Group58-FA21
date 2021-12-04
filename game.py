import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import entities
import objects
import window
import camera

win = window.WINDOW
camera = camera.Camera()

# set up background
BACKGROUND_WIDTH = window.WIDTH
BACKGROUND_HEIGHT = window.HEIGHT
BACKGROUND = pygame.image.load(os.path.join('images/bg2.png'))
BACKGROUNDIMAGE = pygame.transform.rotate(pygame.transform.scale(BACKGROUND, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT)),0)

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
        entities.get_entity_list().update()
        # draw objects onto screen
        camera.update()
        objects.get_object_list().draw(win)
        # draw all sprites onto screen
        entities.get_entity_list().draw(win)

        pygame.display.update()

    pygame.quit()

main()