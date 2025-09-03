import pygame
import numpy as np
from constants import GREY, WHITE, ROWS, COLS, SQUARE_SIZE, scale_x, scale_y
from pieces import images


class Board:
    def __init__(self):
        
        self.board = np.array([
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ])
        self.white_to_move = True
        
    def draw_board(self, screen):
        screen.fill(GREY)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(screen, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE,
                                                    SQUARE_SIZE,     SQUARE_SIZE))
                
    def draw_pieces(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row, col] != '--':
                    print(f"Found piece at [{row},{col}]: {self.board[row, col]}")
                    piece = self.board[row, col]
                    
                    # Center the piece in the square
                    x = col * SQUARE_SIZE + (SQUARE_SIZE - scale_x) // 2
                    y = row * SQUARE_SIZE + (SQUARE_SIZE - scale_y) // 2
                    
                    screen.blit(images[piece], (x, y))
                    
        