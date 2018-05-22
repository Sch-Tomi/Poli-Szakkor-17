import pygame

from Map import Map
from Ship import Ship
from Asteroid import Asteroid
from Bullet import Bullet

class Game:
    def __init__(self):
        self.space = Map()
        
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode((self.space.width, self.space.height))
        pygame.display.set_caption("SpaceShooter")

        self.asteroids = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.allSprites = pygame.sprite.Group()
        self.ship = Ship()
        self.allSprites.add(self.ship)
        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.maxAsteroidsNumber = 10

        self.mainLoop()

    def mainLoop(self):
        running = True
        while running:
            
            self.__checkAsteroidsNumber()

            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.ship.move("L")
                    if event.key == pygame.K_d:
                        self.ship.move("R")
                    if event.key == pygame.K_SPACE:
                        self.ship.shoot()
                        ship_position = self.ship.get_position()
                        b = Bullet(ship_position['x'], ship_position['y'])
                        self.bullets.add(b)
                        self.allSprites.add(b)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.ship.stop()

            self.allSprites.update()


            pygame.sprite.groupcollide(self.bullets, self.asteroids, True, True)
            if pygame.sprite.spritecollide(self.ship, self.asteroids, False):
                running = False

            self.window.fill((0,0,0))
            self.allSprites.draw(self.window)
            pygame.display.flip()

        pygame.quit()

    def __checkAsteroidsNumber(self):
        if len(self.asteroids) < self.maxAsteroidsNumber:
            asteroid = Asteroid()
            self.allSprites.add(asteroid)
            self.asteroids.add(asteroid)


if __name__ == '__main__':
    Game()

