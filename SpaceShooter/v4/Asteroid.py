import pygame
from os import path
import random
from Map import Map


class Asteroid(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.MAP_WIDTH = Map().width
        self.MAP_HEIGHT = Map().height
        
        self.image = self.__loadImage()
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(self.MAP_WIDTH - self.rect.width)
        self.rect.centery = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 7)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.centery += self.speedy
        self.rect.centerx += self.speedx
        if self.rect.centery > self.MAP_HEIGHT + 30:
            self.kill()
        if self.rect.centerx < -30 or self.rect.centerx > self.MAP_WIDTH + 30:
            self.kill()


    def __loadImage(self):
        image_path = path.join(path.dirname(__file__), 'img', 'meteorBrown_med1.png')
        image = pygame.image.load(image_path).convert_alpha()
        #image = pygame.transform.scale(image, (50, 38))
        return image