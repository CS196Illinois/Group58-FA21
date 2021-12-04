import pygame
import os

# extends Sprite to make collision detection easier
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, collidable, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = image.get_rect()
        self.x, self.y = x, y

        self.collidable = collidable

        self.width = image.get_width()
        self.height = image.get_height()

        self.left = x
        self.right = x + self.width
        self.bottom = y
        self.top = y + self.height
