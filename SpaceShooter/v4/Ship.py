import pygame
from os import path

class Ship(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.__loadImage()
        self.rect = self.image.get_rect()
        self.rect.centerx = 240
        self.rect.bottom = 580
        self.speedx = 0
        self.shoot_sound = path.join(path.dirname(__file__), 'sound', 'pew.wav')

    def update(self):
        self.__checkBorder()
        self.rect.x += self.speedx

    def stop(self):
        self.speedx = 0

    def shoot(self):
        pygame.mixer.Sound(self.shoot_sound).play()

    def move(self, direction):
        if direction == "L":
            self.speedx = -5
        elif direction == "R":
            self.speedx = 5
    
    def get_position(self):
        return {'x': self.rect.centerx , 'y':self.rect.centery}
    
    def __loadImage(self):
        image_path = path.join(path.dirname(__file__), 'img', 'ship.png')
        image = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.scale(image, (50, 38))
        return image

    def __checkBorder(self):
        if self.rect.x < 10:
            self.speedx = 0
            self.rect.x = 10
        if self.rect.right > 470:
            self.speedx = 0
            self.rect.right = 470
