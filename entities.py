import os
import pygame
import input
# import objects
import map

MAP_WIDTH = 1500


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


GRAVITY = -0.03
MIN_Y_VEL = -2.5

# Extends from pygame class Sprite
# Allows entity to contain a rect with many useful position variables (look at documentation)
class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        # super(Entity, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        # width and height of sprite set when the image is loaded
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.x_vel, self.y_vel = 0, 0
        self.x_acc, self.y_acc = 0, 0

        self.width = image.get_width()
        self.height = image.get_height()
        self.left = x
        self.right = x + self.width
        self.bottom = y
        self.top = y + self.width
        
    def check_collision(self, object):
        return self.left < object.right and self.bottom < object.top and self.right > object.left and self.top > object.bottom  
    
    # checks collisions between entity and an object after the object moves in the x direction, 
    # returning it to its original location
    def check_collision_x(self, object):
        if self.check_collision(object) and object.collidable:
            if (self.x_vel > 0):
                self.x = object.left - self.width
            else:
                self.x = object.right
        self.left = self.x
        self.right = self.x + self.width
        
            
    # checks collisions between entity and an object after the object moves in the y direction, 
    # returning it to its original location
    def check_collision_y(self, object):
        if self.check_collision(object) and object.collidable:
            if (self.y_vel > 0):
                self.y = object.bottom - self.height
            else:
                self.y = object.top
                self.y_vel = 0
        self.bottom = self.y
        self.top = self.y + self.height

    # update x and y position of entity, prevent it from going off the map and check collisions 
    def update(self):
        # change x and y based on x and y velocity
        self.x_vel += self.x_acc
        self.y_vel += self.y_acc + GRAVITY
        if (self.y_vel < MIN_Y_VEL):
            self.y_vel = MIN_Y_VEL

        self.x += self.x_vel
        self.left = self.x
        self.right = self.x + self.width
        for obj in OBJECT_LIST:
            self.check_collision_x(obj)

        self.y += self.y_vel
        self.bottom = self.y
        self.top = self.y + self.height
        for obj in OBJECT_LIST:
            self.check_collision_y(obj)

        if (self.x < 0):
            self.x = 0
        if (self.y < 0):
            self.y = 0
            self.y_vel = 0

# Primary Mario/player class, extends Entity and Sprite
class Mario(Entity):
    def __init__(self, x, y, image):
        
        super().__init__(x, y, image)

    # sets Mario's velocity based on which input is being given
    def handle_input(self):
        arrayPosition = boswer.getPosition()
        keys = input.keys_pressed()
        if(keys[input.LEFT]):
            self.x_vel = -1.25
        elif(keys[input.RIGHT]):
            self.x_vel = 1.25
        else:
            self.x_vel = 0
        if(keys[input.UP] and self.y_vel == 0):
            self.y_vel = 2.6
        # down key currently has no use
        elif(keys[input.DOWN]):
            pass
        else:
            self.y_vel = self.y_vel
        
        
        # collisons
        if (self.x > arrayPosition[0] and self.x < arrayPosition[1] and self.y == arrayPosition[2]):
            print("YOU HAVE LOST")
            self.x = 0
            self.y = 200 + MARIO_HEIGHT / 2
            


        # if (self.x >= objectPosition[0][0] and self.x <= objectPosition[0][1] and self.x >= objectPosition[0][2] and self.x <= objectPosition[0][3]):
        #     print("YOU HAVE LOST")
        #     self.x = 0
        #     self.y = 200 + MARIO_HEIGHT / 2
        
        # if (self.x >= objectPosition[1][0] and self.x <= objectPosition[1][1] and self.x >= objectPosition[1][2] and self.x <= objectPosition[1][3]):
        #     print("YOU HAVE LOST")
        #     self.x = 0
        #     self.y = 200 + MARIO_HEIGHT / 2

        


    # override Entity update
    # handles input, sets Mario's x and y value as well as Mario's position on the screen
    def update(self):
        self.handle_input()
        super().update()



class Boswer(Entity):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)

   
    def handle_input(self):
        self.x_vel = -.1
        if (self.x == 0):
            self.x = 700

        

    def update(self):
        self.handle_input()
        super().update()

    def getPosition(self):

        positionArray = [0,0, 0]

        positionArray[0]= self.x
        positionArray[1] = self.x + MARIO_WIDTH
        positionArray[2] = self.y
        

        return positionArray

# Initilize entity list with Mario and other entities later




# def get_entity_list():
#     return entity_list

# def get_mario():
#     return mario

# def get_boswer():
#     return boswer




# entities in map
MARIO_WIDTH = 55
MARIO_HEIGHT = 40
MARIO_IMAGE_LOAD = pygame.image.load(os.path.join('images/mario.png'))
MARIO_IMAGE = pygame.transform.rotate(pygame.transform.scale(MARIO_IMAGE_LOAD, (MARIO_WIDTH, MARIO_HEIGHT)),0)


BOSWER_IMAGE_LOAD = pygame.image.load(os.path.join('images/boswer.png'))
BOSWER_IMAGE = pygame.transform.rotate(pygame.transform.scale(BOSWER_IMAGE_LOAD,(55, 40)),0)



ENTITY_LIST = pygame.sprite.Group()
MARIO = Mario(400 - MARIO_WIDTH / 2, 200 + MARIO_HEIGHT / 2, MARIO_IMAGE)
ENTITY_LIST.add(MARIO)
boswer = Boswer(1000,  200 + MARIO_HEIGHT / 2, BOSWER_IMAGE)
ENTITY_LIST.add(boswer)

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
FLAG = Object(1450, 60, False, FLAG_IMAGE)
OBJECT_LIST = pygame.sprite.Group()

OBJECT_LIST.add(FLAG)
for i in range(0, 25):
    OBJECT_LIST.add(Object(0+i*TILE_WIDTH, 0, True, TILE_IMAGE))
OBJECT_LIST.add(Object(300, 60, True, PIPE_IMAGE))
OBJECT_LIST.add(Object(500, 60, True, PIPE_IMAGE))
OBJECT_LIST.add(Object(700, 60, True, PIPE_IMAGE))
OBJECT_LIST.add(Object(760, 60, True, PIPE_IMAGE))
OBJECT_LIST.add(Object(760, 120, True, PIPE_IMAGE))
OBJECT_LIST.add(Object(1000, 100, True, PIPE_IMAGE))
OBJECT_LIST.add(Object(1000, 160, True, PIPE_IMAGE))



