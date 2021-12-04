import pygame
import os

from map import TILE_WIDTH, TILE_IMAGE, PIPE_IMAGE, PIPE_HEIGHT, PIPE_WIDTH 


# extends Sprite to make collision detection easier
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, collidable, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.x, self.y = x, y

        self.collidable = collidable

        # self.width = image.get_width()
        # self.height = image.get_height()

        # self.left = x
        # self.right = x + self.width
        # self.bottom = y
        # self.top = y + self.height
        self.left = x
        self.right = x + image.get_width()
        self.bottom = y
        self.top = y + image.get_height()

# object_list = pygame.sprite.Group()
# for i in range(0, 30):
#     object_list.add(Object(0+i*TILE_WIDTH, 0, True, TILE_IMAGE))
    

# object_list.add(Object(600, 0, True, PIPE_IMAGE))
# object_list.add(Object(250, 0, True, PIPE_IMAGE))


# def get_object_list():
#     return object_list

# def get_object_positionArray():
#     objectPositionArray = [[0,0,0,0],[0,0,0,0]]

#     objectPositionArray[0][0] = 0 # y
#     objectPositionArray[0][1] = PIPE_HEIGHT
#     objectPositionArray[0][2] = 250
#     objectPositionArray[0][3] = 250 + PIPE_WIDTH

#     objectPositionArray[1][0] = 0 # y
#     objectPositionArray[1][1] = PIPE_HEIGHT
#     objectPositionArray[1][2] = 600
#     objectPositionArray[1][3] = 600 + PIPE_WIDTH

#     return objectPositionArray
