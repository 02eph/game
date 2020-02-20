import sys
import pygame

def run_game():
    #иницилизация игры и создание объекта экрана
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #отображение последнего прорисованного экрана
        pygame.display.flip()

run_game()
