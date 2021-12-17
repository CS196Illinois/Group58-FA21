# import pygame
# import os

# # from map import TILE_WIDTH, TILE_IMAGE, PIPE_IMAGE, PIPE_HEIGHT, PIPE_WIDTH 
# import entities

# MAP_WIDTH = 1500

# # entities in map
# MARIO_WIDTH = 55
# MARIO_HEIGHT = 40
# MARIO_IMAGE_LOAD = pygame.image.load(os.path.join('images/mario.png'))
# MARIO_IMAGE = pygame.transform.rotate(pygame.transform.scale(MARIO_IMAGE_LOAD, (MARIO_WIDTH, MARIO_HEIGHT)),0)

# ENTITY_LIST = pygame.sprite.Group()
# MARIO = entities.Mario(400 - MARIO_WIDTH / 2, 200 + MARIO_HEIGHT / 2, MARIO_IMAGE)
# ENTITY_LIST.add(MARIO)

# # objects in map
# TILE_WIDTH = 60
# TILE_HEIGHT = 60
# TILE_IMAGE_LOAD = pygame.image.load(os.path.join('images/floor_tile.png'))
# TILE_IMAGE =  pygame.transform.rotate(pygame.transform.scale(TILE_IMAGE_LOAD, (TILE_WIDTH, TILE_HEIGHT)),0)

# PIPE_WIDTH = 50
# PIPE_HEIGHT = 100
# PIPE_IMAGE_LOAD = pygame.image.load(os.path.join('images/pipe1.png'))
# PIPE_IMAGE = pygame.transform.rotate(pygame.transform.scale(PIPE_IMAGE_LOAD,(PIPE_WIDTH, PIPE_HEIGHT)),0)

# FLAG_HEIGHT = 200
# FLAG_WIDTH = 50
# FLAG_IMAGE_LOAD = pygame.image.load(os.path.join('images/flag.png'))
# FLAG_IMAGE = pygame.transform.rotate(pygame.transform.scale(FLAG_IMAGE_LOAD,(FLAG_WIDTH, FLAG_HEIGHT)),0)
# FLAG = objects.Object(1450, 60, False, FLAG_IMAGE)
# OBJECT_LIST = pygame.sprite.Group()

# OBJECT_LIST.add(FLAG)
# for i in range(0, 25):
#     OBJECT_LIST.add(objects.Object(0+i*TILE_WIDTH, 0, True, TILE_IMAGE))
# OBJECT_LIST.add(objects.Object(300, 60, True, PIPE_IMAGE))
# OBJECT_LIST.add(objects.Object(500, 60, True, PIPE_IMAGE))
# OBJECT_LIST.add(objects.Object(700, 60, True, PIPE_IMAGE))
# OBJECT_LIST.add(objects.Object(760, 60, True, PIPE_IMAGE))
# OBJECT_LIST.add(objects.Object(760, 120, True, PIPE_IMAGE))
# OBJECT_LIST.add(objects.Object(1000, 100, True, PIPE_IMAGE))
# OBJECT_LIST.add(objects.Object(1000, 160, True, PIPE_IMAGE))

# # extends Sprite to make collision detection easier
# class Object(pygame.sprite.Sprite):
#     def __init__(self, x, y, collidable, image):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = image
#         self.rect = image.get_rect()
#         self.x, self.y = x, y

#         self.collidable = collidable

#         # self.width = image.get_width()
#         # self.height = image.get_height()

#         # self.left = x
#         # self.right = x + self.width
#         # self.bottom = y
#         # self.top = y + self.height
#         self.left = x
#         self.right = x + image.get_width()
#         self.bottom = y
#         self.top = y + image.get_height()

# # object_list = pygame.sprite.Group()
# # for i in range(0, 30):
# #     object_list.add(Object(0+i*TILE_WIDTH, 0, True, TILE_IMAGE))
    

# # object_list.add(Object(600, 0, True, PIPE_IMAGE))
# # object_list.add(Object(250, 0, True, PIPE_IMAGE))


# # def get_object_list():
# #     return object_list

# # def get_object_positionArray():
# #     objectPositionArray = [[0,0,0,0],[0,0,0,0]]

# #     objectPositionArray[0][0] = 0 # y
# #     objectPositionArray[0][1] = PIPE_HEIGHT
# #     objectPositionArray[0][2] = 250
# #     objectPositionArray[0][3] = 250 + PIPE_WIDTH

# #     objectPositionArray[1][0] = 0 # y
# #     objectPositionArray[1][1] = PIPE_HEIGHT
# #     objectPositionArray[1][2] = 600
# #     objectPositionArray[1][3] = 600 + PIPE_WIDTH

# #     return objectPositionArray
