import pygame

WIDTH = 1000
HEIGHT = 1000
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

main()
