import os
import pygame
import input

# Mario size
MARIO_WIDTH = 55
MARIO_HEIGHT = 40
MARIO_IMAGE_LOAD = pygame.image.load(os.path.join('mario.png'))
MARIO_IMAGE = pygame.transform.rotate(pygame.transform.scale(MARIO_IMAGE_LOAD, (MARIO_WIDTH, MARIO_HEIGHT)),0)

# Extends from pygame class Sprite
# Allows entity to contain a rect with many useful position variables (look at documentation)
class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.x_vel, self.y_vel = 0, 0
        self.rect.center = (x,y)
        
    # TODO
    # should update entity x and y based on entity's x and y coordinates and potentially
    # detect collisions unless that can be handled by the sprite group
    def update(self):
        pass
        

# Primary Mario/player class, extends Entity and Sprite
class Mario(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, MARIO_IMAGE)

    # sets Mario's velocity based on which input is being given
    # probably better placed in the input.py file if possible
    def handle_input(self):
        keys = input.keys_pressed()
        if(keys[input.LEFT]):
            self.x_vel = -1
        elif(keys[input.RIGHT]):
            self.x_vel = 1
        else:
            self.x_vel = 0
        if(keys[input.UP]):
            self.y_vel = 1
        elif(keys[input.DOWN]):
            self.y_vel = -1
        else:
            self.y_vel = 0

    # override Entity update
    # handles input, sets Mario's x and y value as well as Mario's position on the screen
    def update(self):
        self.handle_input()
        # change x and y based on x and y velocity
        self.x += self.x_vel
        self.y += self.y_vel

        # negative y so that Mario's x and y coordinates are based on the mathematical x and y-axis
        # but Mario can still be formatted correctly
        # i.e. bottom left corner of the screen is Mario's (0, 0) instead of top right
        # better placement is in entity's update method because all entities will use this
        self.rect.center = (self.x, -self.y)
        
        
# Initilize entity list with Mario and other entities later
entity_list = pygame.sprite.Group()
mario = Mario(400, -200)
entity_list.add(mario)

def get_entity_list():
    return entity_list