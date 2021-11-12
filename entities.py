import os
import pygame
import input
import objects

# Mario size
MARIO_WIDTH = 55
MARIO_HEIGHT = 40
MARIO_IMAGE_LOAD = pygame.image.load(os.path.join('images/mario.png'))
MARIO_IMAGE = pygame.transform.rotate(pygame.transform.scale(MARIO_IMAGE_LOAD, (MARIO_WIDTH, MARIO_HEIGHT)),0)

GRAVITY = -0.03
MIN_Y_VEL = -2.5

# Extends from pygame class Sprite
# Allows entity to contain a rect with many useful position variables (look at documentation)
class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        # width and height of sprite set when the image is loaded
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.x_vel, self.y_vel = 0, 0
        self.x_acc, self.y_acc = 0, 0
        
    # update x and y position of entity, prevent it from going off the map and check collisions 
    def update(self):
        # change x and y based on x and y velocity
        self.x_vel += self.x_acc
        self.y_vel += self.y_acc + GRAVITY
        if (self.y_vel < MIN_Y_VEL):
            self.y_vel = MIN_Y_VEL

        self.x += self.x_vel
        self.y += self.y_vel
        if (self.x < 0):
            self.x = 0
        if (self.y < 0):
            self.y = 0
            self.y_vel = 0



# Primary Mario/player class, extends Entity and Sprite
class Mario(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, MARIO_IMAGE)

    # sets Mario's velocity based on which input is being given
    def handle_input(self):
        keys = input.keys_pressed()
        if(keys[input.LEFT]):
            self.x_vel = -1
        elif(keys[input.RIGHT]):
            self.x_vel = 1
        else:
            self.x_vel = 0
        if(keys[input.UP] and self.y_vel == 0):
            self.y_vel = 3.25
        # down key currently has no use
        elif(keys[input.DOWN]):
            pass
        else:
            self.y_vel = self.y_vel

    # override Entity update
    # handles input, sets Mario's x and y value as well as Mario's position on the screen
    def update(self):
        self.handle_input()
        super().update()

 
# Initilize entity list with Mario and other entities later
entity_list = pygame.sprite.Group()
mario = Mario(400 - MARIO_WIDTH / 2, 200 + MARIO_HEIGHT / 2)
entity_list.add(mario)

def get_entity_list():
    return entity_list

def get_mario():
    return mario