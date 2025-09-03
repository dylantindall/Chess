import pygame
from constants import scale_x, scale_y

piece_types= ['bR','bN','bB','bK','bQ','bp',
              'wR','wN','wB','wK','wQ','wp']

# Create a dictionary to store the image pieces from the PNG folder.
images = {}
for piece in piece_types:
    images[piece] = pygame.transform.scale(
        pygame.image.load('piecesPNG/'+str(piece)+'.png'), (scale_x, scale_y)
    )

# set up a pieces class to initialise colour and location:

class Piece:
    def __init__(self, type):
        if type.startswith('w'):
            self.colour = 'White'
        else:
            self.colour = 'Black'
            
        self.image = images(type)

    def valid_moves(self, row, col):
        self.row = row
        self.col = col


      
# class Pawn(Piece):

# class Knight(Piece):

# class Bishop(Piece):
    
# class Rook(Piece):
    
# class Queen(Piece):
    
# class King(Piece):