import pygame

# correspond to the index where boolean values for specific inputs are stored
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

# returns a boolean array of inputs: true if the input is being activated, false otherwise
def keys_pressed():
    # array of booleans for each key on the keyboard
    # boolean is True if the key is pressed and false otherwise
    keys=pygame.key.get_pressed()
    k_array=[False,False,False,False]

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        k_array[LEFT] = True
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
        k_array[RIGHT] = True
    if (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]):
        k_array[UP] = True
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]):
        k_array[DOWN] = True

    return k_array