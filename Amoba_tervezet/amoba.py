#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import os
import amoba_lib

# Initialize pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Jatekter hattere
TABLA = [[0]*10 for i in range(10)]
JATEKOS = 1

# Képernyő felbontás és ablak méret beállítás
SCREEN_SIZE = (pygame.display.Info().current_w, pygame.display.Info().current_h)
WINDOW_SIZE = (555, 600)
MARGIN = 5
WIDTH = 50
HEIGHT = 50

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
font_win = pygame.font.Font(None, 35)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

ingame = False

match_going = True

while not ingame:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            ingame = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            if TABLA[row][column] == 0:
                TABLA[row][column] = JATEKOS
                #print("Click ", pos, "Grid coordinates: ", row, column, TABLA)
                JATEKOS = 1 if JATEKOS == 2 else 2
                if amoba_lib.check(TABLA, 3):
                    match_going = False

    # Set the screen background
    screen.fill(BLACK)
    if match_going:
        # Draw the grid
        for row in range(10):
            for column in range(10):
                color = WHITE
                if TABLA[row][column] == 1:
                    color = GREEN
                elif TABLA[row][column] == 2:
                    color = RED
                pygame.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])
        
        #Kikövetkezik:
        jatekos_txt = "zöld" if JATEKOS == 1 else "piros"
        out_txt = "Következő játékos: " + jatekos_txt
        text = font.render(out_txt,True,RED)
        screen.blit(text, [WINDOW_SIZE[0]/2 - 100,WINDOW_SIZE[1]-30])

        # Limit to 60 frames per second
        clock.tick(60)
    else:
        nyertes_txt = "piros" if JATEKOS == 1 else "zöld"
        out_txt = "A nyertes a " + nyertes_txt + " játékos!"
        text = font_win.render(out_txt,True,RED)
        screen.blit(text, [WINDOW_SIZE[0]/2 - font_win.size(out_txt)[0]/2, WINDOW_SIZE[1]/2-font_win.size(out_txt)[1]])

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

