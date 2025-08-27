import pygame
import sys
import os
import numpy as np
from .constants import WIDTH, HEIGHT
from board import Board



# create a class to define a piece:
# attributes: colour, piece, location

# create the chess board:

# Screen setup

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")        


#define framerate:
FPS = 60

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():

            # check if game is active.
            if event.type == pygame.QUIT:
                run = False

            # check if mouse has been clicked.
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_board(screen)

    pygame.quit()


main()