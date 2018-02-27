#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import os
from snake_lib import snakeLib

# Initialize pygame
pygame.init()

#Init snake
snake = snakeLib()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 153, 51)
GREEN2 = (51, 204, 51)
RED = (255, 0, 0)

# Képernyő felbontás és ablak méret beállítás
SCREEN_SIZE = (pygame.display.Info().current_w, pygame.display.Info().current_h)
WINDOW_SIZE = (515, 600)
MARGIN = 2
WIDTH = 15
HEIGHT = 15

# Középen nyissa meg
pos_x = SCREEN_SIZE[0] / 2 - WINDOW_SIZE[0] / 2
pos_y = SCREEN_SIZE[1] / 2 - WINDOW_SIZE[1]
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y)
os.environ['SDL_VIDEO_CENTERED'] = '0'
 
# Set the HEIGHT and WIDTH of the screen
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Amőba")

# Kiiráshoz:
font = pygame.font.Font(None, 25)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

ingame = False

match_going = True

snake_moved = False

apple_tick = 0

START = False

while not ingame:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            ingame = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.move("L") 
            if event.key == pygame.K_RIGHT:
                snake.move("R")
            if event.key == pygame.K_UP:
                snake.move("U")
            if event.key == pygame.K_DOWN:
                snake.move("D")
            if event.key == pygame.K_SPACE:
                START = True

            snake_moved = True
        
    # Set the screen background
    screen.fill(BLACK)
    # Draw the grid
    for row in range(30):
        for column in range(30):
            field = snake.get_field()
            
            if field[row][column] == "S":
                color = GREEN2
                if snake.get_snake_head()[0] == row and snake.get_snake_head()[1] == column:
                    color = GREEN
            elif field[row][column] == "A":
                color = RED
            else:
                color = BLACK
            pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])

    pygame.draw.line(screen, WHITE, [0,0], [512,0], 3)
    pygame.draw.line(screen, WHITE, [0,0], [0,510], 3)
    pygame.draw.line(screen, WHITE, [512,0], [512,510], 3)
    pygame.draw.line(screen, WHITE, [0,510], [512,510], 3)

    # Limit to 60 frames per second
    clock.tick(10)

    if START:

        # RUSH B effect
        if snake_moved:
            snake_moved = False
        else:
            snake.move()

        # Hogy legyen 3 alma
        if snake.get_apples_number() < 3:
            snake.random_apple()

        # Régi almák eltüntetése
        if apple_tick == 10:
            snake.remove_old_apple()
            apple_tick = 0
        else:
            apple_tick += 1

        #Pontszám
        out_txt = "Pontszám: " + str(snake.get_snake_length() - 3)
        text = font.render(out_txt,True,RED)
        screen.blit(text, [WINDOW_SIZE[0]/2 - 50,WINDOW_SIZE[1]-30])

        # Vége szöveg
        if not snake.is_alive():
            out_txt = "Vége!!!"
            text = font.render(out_txt,True,RED)
            screen.blit(text, [WINDOW_SIZE[0]/2 - 35,WINDOW_SIZE[1] - 60])
    else:
        #Pontszám
        out_txt = "SPACE-re indul!!"
        text = font.render(out_txt,True,RED)
        screen.blit(text, [WINDOW_SIZE[0]/2 - 50,WINDOW_SIZE[1]-30])

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
