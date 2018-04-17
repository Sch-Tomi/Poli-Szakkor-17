import pygame

class Ship(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 240
        self.rect.bottom = 580
        self.speedx = 0

    def update(self):
        pass
    