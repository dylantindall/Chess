import pygame
from .constants import BLACK, WHITE, ROWS, COLS, SQUARE_SIZE

class Board:
    def __init__(self);
        self.board = np.array([
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bB"],
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
        screen.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2)
                pygame.draw.rect(screen, WHITE (row*SQUARE_SIZE, col*SQUARE_SIZE,
                                                    SQUARE_SIZE,     SQUARE_SIZE))
                

        