import pygame
import entities
import os
import objects

MAP_WIDTH = 1500

# entities in map
MARIO_WIDTH = 55
MARIO_HEIGHT = 40
MARIO_IMAGE_LOAD = pygame.image.load(os.path.join('images/mario.png'))
MARIO_IMAGE = pygame.transform.rotate(pygame.transform.scale(MARIO_IMAGE_LOAD, (MARIO_WIDTH, MARIO_HEIGHT)),0)

ENTITY_LIST = pygame.sprite.Group()
MARIO = entities.Mario(400 - MARIO_WIDTH / 2, 200 + MARIO_HEIGHT / 2, MARIO_IMAGE)
ENTITY_LIST.add(MARIO)

# objects in map
TILE_WIDTH = 60
TILE_HEIGHT = 60
TILE_IMAGE_LOAD = pygame.image.load(os.path.join('images/floor_tile.png'))
TILE_IMAGE =  pygame.transform.rotate(pygame.transform.scale(TILE_IMAGE_LOAD, (TILE_WIDTH, TILE_HEIGHT)),0)

PIPE_WIDTH = 50
PIPE_HEIGHT = 100
PIPE_IMAGE_LOAD = pygame.image.load(os.path.join('images/pipe1.png'))
PIPE_IMAGE = pygame.transform.rotate(pygame.transform.scale(PIPE_IMAGE_LOAD,(PIPE_WIDTH, PIPE_HEIGHT)),0)

FLAG_HEIGHT = 200
FLAG_WIDTH = 50
FLAG_IMAGE_LOAD = pygame.image.load(os.path.join('images/flag.png'))
FLAG_IMAGE = pygame.transform.rotate(pygame.transform.scale(FLAG_IMAGE_LOAD,(FLAG_WIDTH, FLAG_HEIGHT)),0)
FLAG = objects.Object(1450, 60, False, FLAG_IMAGE)
OBJECT_LIST = pygame.sprite.Group()

OBJECT_LIST.add(FLAG)
for i in range(0, 25):
    OBJECT_LIST.add(objects.Object(0+i*TILE_WIDTH, 0, True, TILE_IMAGE))
OBJECT_LIST.add(objects.Object(300, 60, True, PIPE_IMAGE))
OBJECT_LIST.add(objects.Object(500, 60, True, PIPE_IMAGE))
OBJECT_LIST.add(objects.Object(700, 60, True, PIPE_IMAGE))
OBJECT_LIST.add(objects.Object(760, 60, True, PIPE_IMAGE))
OBJECT_LIST.add(objects.Object(760, 120, True, PIPE_IMAGE))
OBJECT_LIST.add(objects.Object(1000, 100, True, PIPE_IMAGE))
OBJECT_LIST.add(objects.Object(1000, 160, True, PIPE_IMAGE))

