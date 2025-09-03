import pygame
import sys
import os
import numpy as np
from constants import WIDTH, HEIGHT, SQUARE_SIZE
from board import Board



# create a class to define a piece:
# attributes: colour, piece, location

# create the chess board:

# Screen setup

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")        

# Convert the mouse position on screen to a tile on the board
def get_tile_from_mouse(pos):

    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return col, row

#define framerate:
FPS = 60

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    selected_piece = None

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():

            # check if game is active.
            if event.type == pygame.QUIT:
                run = False

            # check if mouse has been clicked.
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                selected_col, selected_row = get_tile_from_mouse(mouse_pos)
                board.find_piece_at(selected_col, selected_row)


        board.draw_board(screen)
        board.draw_pieces(screen)
        pygame.display.update()

    pygame.quit()


main()