import pygame

from Map import Map
from Ship import Ship

class Game:
    def __init__(self):
        self.space = Map()
        
        pygame.init()
        self.window = pygame.display.set_mode((self.space.width, self.space.height))
        pygame.display.set_caption("SpaceShooter")

        self.allSprites = pygame.sprite.Group()
        self.ship = Ship()
        self.allSprites.add(self.ship)
        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.mainLoop()

    def mainLoop(self):
        running = True
        while running:
            
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.ship.move("L")
                    if event.key == pygame.K_d:
                        self.ship.move("R")
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.ship.stop()

            self.allSprites.update()

            self.window.fill((0,0,0))
            self.allSprites.draw(self.window)
            pygame.display.flip()

        pygame.quit()



if __name__ == '__main__':
    Game()

