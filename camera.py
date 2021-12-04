import pygame
import window
import map

MAX_X = map.MAP_WIDTH
mario = map.MARIO

class Camera():
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self):
        self.x = mario.x + mario.width / 2 - window.WIDTH / 2
        self.y = mario.y + mario.height / 2 - window.HEIGHT / 2

        if (mario.x < window.WIDTH / 2 - mario.width / 2): 
            self.x = 0
        if (mario.x > MAX_X - window.WIDTH / 2 - mario.width / 2):
            self.x = MAX_X - window.WIDTH
        if (mario.y < window.HEIGHT / 2 - mario.height / 2):
            self.y = 0
        
        for entity in map.ENTITY_LIST:
            entity.rect.bottomleft = (entity.x + -self.x, -entity.y + window.HEIGHT + self.y)
                
        for object in map.OBJECT_LIST:
            object.rect.bottomleft = (object.x + -self.x, -object.y + window.HEIGHT + self.y)
