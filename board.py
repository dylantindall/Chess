import pygame
import numpy as np
from constants import GREY, WHITE, ROWS, COLS, SQUARE_SIZE, scale_x, scale_y
from pieces import white_images, black_images, Piece, Pawn, Knight, Bishop, Rook, Queen, King



class Board:
    def __init__(self):
        
        self.board = np.empty((8, 8), dtype=object)

        # Set up pawns on the board
        for i in range(8):
            for j in range(8):

                # Initialise black back rank pieces
                if i == 0:
                    if   j == 0 or j == 7:
                        self.board[i][j] = Rook('Black', i, j)
                    elif j == 1 or j == 6:
                        self.board[i][j] = Knight('Black', i, j)
                    elif j == 2 or j == 5:
                        self.board[i][j] = Bishop('Black', i, j)
                    elif j == 3:
                        self.board[i][j] = Queen('Black', i, j)
                    elif j == 4:
                        self.board[i][j] = King('Black', i, j)

                # Initialise black pawns
                elif i == 1:
                    self.board[i][j] = Pawn('Black', i, j)

                # Initialise white back rank pieces
                elif i == 7:
                    if   j == 0 or j == 7:
                        self.board[i][j] = Rook('White', i, j)
                    elif j == 1 or j == 6:
                        self.board[i][j] = Knight('White', i, j)
                    elif j == 2 or j == 5:
                        self.board[i][j] = Bishop('White', i, j)
                    elif j == 3:
                        self.board[i][j] = Queen('White', i, j)
                    elif j == 4:
                        self.board[i][j] = King('White', i, j)
                
                # Initialise white pawns
                elif i == 6:
                    self.board[i][j] = Pawn('White', i, j)

                # Initialise empty tiles
                else:
                    self.board[i][j] = None

                
        self.colour_to_move = 'White'
        self.captured_pieces = list()
        
    def draw_board(self, screen):
        screen.fill(GREY)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(screen, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE,
                                                    SQUARE_SIZE,     SQUARE_SIZE))
                
    def draw_pieces(self, screen):

        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row, col] != None:

                    piece = self.board[row, col]
                    
                    # Center the piece in the square
                    x = col * SQUARE_SIZE + (SQUARE_SIZE - scale_x) // 2
                    y = row * SQUARE_SIZE + (SQUARE_SIZE - scale_y) // 2
                    
                    if piece.colour == 'White':
                        screen.blit(white_images[('w' + str(piece))], (x, y))

                    if piece.colour == 'Black':
                        screen.blit(black_images[('b' + str(piece))], (x, y))

    def find_piece_at(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            if self.board[row, col].startswith(self.colour):
                return self.board[row, col]
        return None

        




                    
        