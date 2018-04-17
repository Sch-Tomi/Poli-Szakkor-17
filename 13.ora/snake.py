#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN_BODY = (0, 153, 51)
GREEN_HEAD = (51, 204, 51)

WINDOW_SIZE = (515, 600)
SCREEN_SIZE = (pygame.display.Info().current_w, 
                pygame.display.Info().current_h)

window = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Snake")

quit = False

while not quit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    window.fill(BLACK)

    #pygame.draw.line(window, RED, [0,0], [515, 600], 5)
    #pygame.draw.line(window, GREEN_BODY, [0,600], [515, 0], 10)

    #pygame.draw.line(window, (123, 244, 155), [0,300], [515,300], 7)

    pygame.draw.rect(window, RED, [50,50, 70, 70])


    pygame.display.flip()

pygame.quit()
