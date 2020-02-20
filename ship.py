import pygame

class Ship():
    def __init__(self, screen):
        """инициализирует корабль и задает его начальную позицию"""
        self.screen = screen

        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1    
            #выводит изображение на экран в позиции заданной self.rect
    def blitme(self):
        self.screen.blit(self.image, self.rect)
