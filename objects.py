import pygame
import os

TILE_WIDTH = 60
TILE_HEIGHT = 60

PIPE_WIDTH = 50
PIPE_HEIGHT = 100

TILE_IMAGE_LOAD = pygame.image.load(os.path.join('images/floor_tile.png'))
TILE_IMAGE =  pygame.transform.rotate(pygame.transform.scale(TILE_IMAGE_LOAD, (TILE_WIDTH, TILE_HEIGHT)),0)

PIPE_IMAGE_LOAD = pygame.image.load(os.path.join('images/pipe1.png'))
PIPE_IMAGE = pygame.transform.rotate(pygame.transform.scale(PIPE_IMAGE_LOAD,(PIPE_WIDTH, PIPE_HEIGHT)),0)



# extends Sprite to make collision detection easier
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, collidable, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.x, self.y = x, y

        self.collidable = collidable

        self.left = x
        self.right = x + image.get_width()
        self.bottom = y
        self.top = y + image.get_height()

object_list = pygame.sprite.Group()
for i in range(0, 30):
    object_list.add(Object(0+i*TILE_WIDTH, 0, True, TILE_IMAGE))
    

object_list.add(Object(600, 0, True, PIPE_IMAGE))
object_list.add(Object(250, 0, True, PIPE_IMAGE))


def get_object_list():
    return object_list

def get_object_positionArray():
    objectPositionArray = [[0,0,0,0],[0,0,0,0]]

    objectPositionArray[0][0] = 0 # y
    objectPositionArray[0][1] = PIPE_HEIGHT
    objectPositionArray[0][2] = 250
    objectPositionArray[0][3] = 250 + PIPE_WIDTH

    objectPositionArray[1][0] = 0 # y
    objectPositionArray[1][1] = PIPE_HEIGHT
    objectPositionArray[1][2] = 600
    objectPositionArray[1][3] = 600 + PIPE_WIDTH

    return objectPositionArray