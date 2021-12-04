import pygame
import entities
import objects
import window

mario = entities.get_mario()

boswer = entities.get_boswer()
class Camera():
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self):
        self.x += mario.x_vel
        self.y += mario.y_vel

        lockx = mario.x < window.WIDTH / 2 - entities.MARIO_WIDTH / 2
        locky = mario.y < window.HEIGHT / 2 + entities.MARIO_HEIGHT / 2
        if (lockx):
            self.x = 0
        if (locky):
            self.y = 0
        
        for entity in entities.get_entity_list():
            if lockx and locky:
                entity.rect.bottomleft = (entity.x, -entity.y + window.HEIGHT)
            elif lockx:
                entity.rect.bottomleft = (entity.x, -entity.y + window.HEIGHT + self.y)
            elif locky:
                entity.rect.bottomleft = (entity.x + -self.x, -entity.y + window.HEIGHT)
            else:
                entity.rect.bottomleft = (entity.x + -self.x, -entity.y + window.HEIGHT + self.y)
            
        for object in objects.get_object_list():
            if lockx and locky:
                object.rect.bottomleft = (object.x, -object.y + window.HEIGHT)
            elif lockx:
                object.rect.bottomleft = (object.x, -object.y + window.HEIGHT + self.y)
            elif locky:
                object.rect.bottomleft = (object.x + -self.x, -object.y + window.HEIGHT)
            else: 
                object.rect.bottomleft = (object.x + -self.x, -object.y + window.HEIGHT + self.y)
