import pygame
from os import path

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = self.__loadImage()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedy = -15

    def update(self):
        self.rect.centery += self.speedy
        if self.rect.bottom < 0:
            self.kill()
    
    def __loadImage(self):
        image_path = path.join(path.dirname(__file__), 'img', 'laser.png')
        image = pygame.image.load(image_path).convert_alpha()
        #image = pygame.transform.scale(image, (50, 38))
        return image