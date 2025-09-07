import pygame
import sys
import os
import numpy as np
from constants import WIDTH, HEIGHT, SQUARE_SIZE
from board import Board

# Initialise pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")        

# Convert the mouse position on screen to a tile on the board
def get_tile_from_mouse(pos):

    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return row, col

#define framerate:
FPS = 60

def main():
    run = True
    clock = pygame.time.Clock()
    game = Board()

    selected_piece = None
    new_selected_piece = None
    valid_moves = list()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():

            # Check if game is active.
            if event.type == pygame.QUIT:
                run = False

            # Check if mouse has been clicked.
            if event.type == pygame.MOUSEBUTTONDOWN:

                # If a piece isn't currently selected, select the new piece
                if selected_piece == None:
                    mouse_pos = pygame.mouse.get_pos()
                    selected_row, selected_col = get_tile_from_mouse(mouse_pos)

                    # Make sure the new piece is the right colour
                    if game.board[selected_row][selected_col] == None:
                        pass
                    elif game.colour_to_move == game.board[selected_row][selected_col].colour:
                        selected_piece = game.board[selected_row][selected_col]
                        # Get all valid moves for the current piece
                        valid_moves = selected_piece.get_valid_moves(game.board)
                    else:
                        pass

                # If a piece is currently selected
                elif selected_piece != None:
                    
                    # Find the new selected piece
                    mouse_pos = pygame.mouse.get_pos()
                    new_selected_row, new_selected_col = get_tile_from_mouse(mouse_pos)
                    new_selected_piece = game.board[new_selected_row][new_selected_col]

                    # Check if the new selection is an empty tile and a valid move.
                    if new_selected_piece is None and (new_selected_row, new_selected_col) in valid_moves:
                                                   
                        # Update the board
                        game.board[new_selected_row][new_selected_col] = selected_piece
                        game.board[selected_piece.row][selected_piece.col] = None
                        # Update position of the selected piece
                        selected_piece.row = new_selected_row
                        selected_piece.col = new_selected_col
                        # Reset selection and change colour to move
                        selected_piece = None
                        new_selected_piece = None
                        game.colour_to_move = 'Black' if game.colour_to_move == 'White' else 'White'

                    elif new_selected_piece is None and (new_selected_row, new_selected_col) not in valid_moves:
                        pass

                    # If the piece is the same colour, change that piece to the selection.
                    elif game.colour_to_move == new_selected_piece.colour:

                        selected_piece = new_selected_piece
                        valid_moves = selected_piece.get_valid_moves(game.board)
                        new_selected_piece = None

                    # Check if new selection is opposing colour and a valid move
                    elif game.colour_to_move == new_selected_piece.opp_colour:
                        if (new_selected_row, new_selected_col) in valid_moves:

                            # Update list of captured pieces
                            game.captured_pieces.append(new_selected_piece)

                            # Update the board
                            game.board[new_selected_row][new_selected_col] = selected_piece
                            game.board[selected_piece.row][selected_piece.col] = None

                            # Update the position of the selected piece
                            selected_piece.row = new_selected_row
                            selected_piece.col = new_selected_col

                            # Reset selections and change turn
                            selected_piece = None
                            new_selected_piece = None
                            game.colour_to_move = 'Black' if game.colour_to_move == 'White' else 'White'

                    else:
                        pass


        game.draw_board(screen)
        game.draw_pieces(screen)
        pygame.display.update()

    pygame.quit()


main()