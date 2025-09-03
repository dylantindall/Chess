import pygame
from constants import scale_x, scale_y, SQUARE_SIZE

piece_types= ['bR','bN','bB','bK','bQ','bp',
              'wR','wN','wB','wK','wQ','wp']

# Create a dictionary to store the image pieces from the PNG folder.
images = {}
for piece in piece_types:
    images[piece] = pygame.transform.scale(
        pygame.image.load('piecesPNG/'+str(piece)+'.png'), (scale_x, scale_y)
    )

# Set up a pieces class.
class Piece:
    def __init__(self, row, col, colour):
        self.colour = colour
        self.opp_colour = 'b' if self.colour == 'w' else 'w'
        self.row = row
        self.col = col
        self.calc_pos()

    def calc_pos(self):
        self.x = self.col * SQUARE_SIZE + (100-scale_x)//2
        self.y = self.row * SQUARE_SIZE + (100-scale_y)//2

    def is_valid_position(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
    

    


# Set up pawn subclass
class Pawn(Piece):

    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)
        self.direction = 0
        self.has_moved = False
        if colour == 'b':
            self.direction = 1
        elif colour == 'w':
            self.direction = -1
    
    def get_valid_moves(self, board):

        valid_moves = []
        new_row = 0
        new_col = 0

        # Check if on borders
        if self.row not in [0, 7]:

            # Check if next tile is empty
            if board[(self.row + self.direction), (self.col)] == '--':

                # Move forward once
                new_row, new_col = self.row, (self.col+ self.direction)
                valid_moves.append((new_x, new_y))

                # Check if pawn hasn't moved and 2nd next tile is empty
                if self.has_moved == False and board[(self.col), (self.row + 2*self.direction)] == '--':

                    # Move forward twice
                    new_x, new_y = self.col, (self.row + 2*self.direction)
                    valid_moves.append((new_x, new_y))
            
            # Check if opposing piece is on the diagonal tiles
            for i in [1,-1]:

                if board[(self.col + i), (self.row + self.direction)].startswith(self.opp_colour):

                    # Capture diagonally
                    new_x, new_y = self.col + i, (self.row + self.direction)
                    valid_moves.append((new_x, new_y))

        return valid_moves


# set up knight subclass
class Knight(Piece):
        
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)
    
    def get_valid_moves(self, board):

        valid_moves = []
        new_x = 0
        new_y = 0

        # List of all possible movement trajectories for a knight
        knight_movements = [( 2, 1),( 2,-1),
                            (-2, 1),(-2, 1),
                            ( 1, 2),( 1,-2),
                            (-1, 2),(-1,-2)]
        
        # Calculate all valid/invalid moves based on current tile.
        all_moves = []
        
        for x_y in knight_movements:

            new_x = self.col + x_y(0)
            new_y = self.row + x_y(1)

            # Check if new tile exists on the board.
            if self.is_valid_position(new_x, new_y):
                
                # Check if tile is empty or piece is available for capture.
                if not board[new_x, new_y].startswith(self.colour):

                    # Add to list of valid moves.
                    valid_moves.append((new_x,new_y))

        return valid_moves

            
            
# set up bishop subclass
class Bishop(Piece):
        
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)
    
    def get_valid_moves(self, board):

        valid_moves = []

        # Loop through trajectories
        for i,j in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            # Reset position
            new_col = self.col
            new_row = self.row

            # Loop through diagonal as long as the next position exists
            while self.is_valid_position(new_col + i, new_row + j):

                new_col += i
                new_row += j

                # If same coloured piece is on next tile, end loop
                if board[new_col, new_row].startswith(self.colour):
                    break

                # If opposing piece on next tile, add capture move and end loop
                elif board[new_col, new_row].startswith(self.opp_colour):
                    valid_moves.append((new_col, new_row))
                    break

                # If next tile is empty, add move and end loop
                else:
                    valid_moves.append((new_col, new_row))

        return valid_moves
                    


# set up Rook subclass
class Rook(Piece):
        
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)
    
    def get_valid_moves(self, board):

        valid_moves = []

        # Loop through trajectories
        for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:

            # Reset position
            new_col = self.col
            new_row = self.row

            # Loop through diagonal as long as the next position exists
            while self.is_valid_position(new_col + i, new_row + j):

                new_col += i
                new_row += j

                # If same coloured piece is on next tile, end loop
                if board[new_col, new_row].startswith(self.colour):
                    break

                # If opposing piece on next tile, add capture move and end loop
                elif board[new_col, new_row].startswith(self.opp_colour):
                    valid_moves.append((new_col, new_row))
                    break

                # If next tile is empty, add move and end loop
                else:
                    valid_moves.append((new_col, new_row))

        return valid_moves
    


class Queen(Piece):

    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)
    
    def get_valid_moves(self, board):

        valid_moves = []

        # Loop through trajectories
        for i,j in [(-1, 1), ( 0, 1), ( 1, 1),
                    (-1, 0),          ( 1, 0),
                    (-1,-1), ( 0,-1), ( 1,-1)]:
            
            # Reset position
            new_col = self.col
            new_row = self.row

            # Loop through diagonal as long as the next position exists
            while self.is_valid_position(new_col + i, new_row + j):

                new_col += i
                new_row += j

                # If same coloured piece is on next tile, end loop
                if board[new_col, new_row].startswith(self.colour):
                    break

                # If opposing piece on next tile, add capture move and end loop
                elif board[new_col, new_row].startswith(self.opp_colour):
                    valid_moves.append((new_col, new_row))
                    break

                # If next tile is empty, add move and end loop
                else:
                    valid_moves.append((new_col, new_row))
        
        return valid_moves
        
    
class King(Piece):

    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)
    
    def get_valid_moves(self, board):

        valid_moves = []

        # Loop through trajectories
        for i,j in [(-1, 1), ( 0, 1), ( 1, 1),
                    (-1, 0),          ( 1, 0),
                    (-1,-1), ( 0,-1), ( 1,-1)]:
            
            # Check if position exists on board
            if self.is_valid_position(self.col + i, self.row + j):

                new_col = self.col + i
                new_row = self.row + j

                # If same coloured piece is on next tile, end loop
                if board[new_col, new_row].startswith(self.colour):
                    break

                # If opposing piece on next tile, add capture move and end loop
                elif board[new_col, new_row].startswith(self.opp_colour):
                    valid_moves.append((new_col, new_row))
                    break

                # If next tile is empty, add move and end loop
                else:
                    valid_moves.append((new_col, new_row))
    
        return valid_moves