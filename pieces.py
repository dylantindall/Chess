import pygame
from constants import scale_x, scale_y, SQUARE_SIZE

piece_types = ['Pawn','Knight','Bishop','King','Queen','Rook']

# Create a dictionary to store the white/black image pieces from the PNG folder.
white_images = {}
for piece in piece_types:
    white_images['w' + piece] = pygame.transform.scale(
        pygame.image.load('piecesPNG/w'+str(piece)+'.png'), (scale_x, scale_y))
    
black_images = {}
for piece in piece_types:
    black_images['b' + piece] = pygame.transform.scale(
        pygame.image.load('piecesPNG/b'+str(piece)+'.png'), (scale_x, scale_y))

# Set up a pieces class.
class Piece:
    def __init__(self, colour, row, col):
        self.colour = colour
        self.opp_colour = 'Black' if self.colour == 'White' else 'White'
        self.row = row
        self.col = col

    def __str__(self):
        return f"{self.__class__.__name__}"


    def is_valid_position(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8
    

    


# Set up pawn subclass
class Pawn(Piece):

    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)
        self.direction = 0
        self.has_moved = False
        if colour == 'Black':
            self.direction = 1
        elif colour == 'White':
            self.direction = -1
    
    def get_valid_moves(self, board):

        valid_moves = []
        new_row = 0
        new_col = 0

        # Check if on borders
        if self.row not in [0, 7]:

            # Check if next tile is empty
            if board[(self.row + self.direction), (self.col)] == None:

                # Move forward once
                new_row, new_col = self.row + self.direction, self.col
                valid_moves.append((new_row, new_col))

                # Check if pawn hasn't moved and 2nd next tile is empty
                if self.has_moved == False and board[(self.row + 2*self.direction), (self.col)] == None:

                    # Move forward twice
                    new_row, new_col = self.row + 2 * self.direction, self.col
                    valid_moves.append((new_row, new_col))
            
            # Check if opposing piece is on the diagonal tiles
            for i in [1,-1]:
                piece_at_position = board[(self.row + self.direction), (self.col + i)]
                if piece_at_position is not None and piece_at_position.colour == self.opp_colour:

                    # Capture diagonally
                    new_row, new_col = (self.row + self.direction), (self.col + i)
                    valid_moves.append((new_row, new_col))

        return valid_moves


# set up knight subclass
class Knight(Piece):
        
    def __init__(self, colour, row, col):
        super().__init__(colour, row, col)
    
    def get_valid_moves(self, board):

        valid_moves = []
        new_row = 0
        new_col = 0

        # List of all possible movement trajectories for a knight
        knight_movements = [( 2, 1),( 2,-1),
                            (-2, 1),(-2,-1),
                            ( 1, 2),( 1,-2),
                            (-1, 2),(-1,-2)]
        
        for x_y in knight_movements:

            new_row = self.row + x_y[0]
            new_col = self.col + x_y[1]

            # Check if new tile exists on the board.
            if self.is_valid_position(new_row, new_col):
                
                # Check if tile is empty or piece is available for capture
                if board[new_row][new_col] == None or board[new_row][new_col].colour == self.opp_colour:

                    # Add to list of valid moves.
                    valid_moves.append((new_row,new_col))

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
            new_row = self.row
            new_col = self.col

            # Loop through diagonal as long as the next position exists
            while self.is_valid_position(new_row + i, new_col + j):

                new_row += i
                new_col += j

                # If tile is empty, add the move and repeat the loop
                if board[new_row][new_col] == None:
                    valid_moves.append((new_col, new_row))

                # If same coloured piece is on next tile, end loop
                elif board[new_row][new_col].colour == self.colour:
                    break

                # If opposing piece on next tile, add capture move and end loop
                elif board[new_row][new_col].colour == self.opp_colour:
                    valid_moves.append((new_row, new_col))
                    break



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
            new_row = self.row
            new_col = self.col
            
            # Loop through moves as long as the next position exists
            while self.is_valid_position(new_col + i, new_row + j):

                new_row += i
                new_col += j

                # If tile is empty, add the move and repeat the loop
                if board[new_row][new_col] == None:
                    valid_moves.append((new_row, new_col))

                # If same coloured piece is on next tile, end loop
                elif board[new_row][new_col].colour == self.colour:
                    break

                # If opposing piece on next tile, add capture move and end loop
                elif board[new_row][new_col].colour == self.opp_colour:
                    valid_moves.append((new_row, new_col))
                    break

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
            new_row = self.row
            new_col = self.col

            # Loop through diagonal as long as the next position exists
            while self.is_valid_position(new_row + i, new_col + j):

                new_row += i
                new_col += j

                # If tile is empty, add the move and repeat the loop
                if board[new_row][new_col] == None:
                    valid_moves.append((new_row, new_col))

                # If same coloured piece is on next tile, end loop
                elif board[new_row][new_col].colour == self.colour:
                    break

                # If opposing piece on next tile, add capture move and end loop
                elif board[new_row][new_col].colour == self.opp_colour:
                    valid_moves.append((new_row, new_col))
                    break

        
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
            if self.is_valid_position(self.row + i, self.col + j):

                new_row = self.row + i
                new_col = self.col + j

                # If tile is empty, add the move and repeat the loop
                if board[new_row][new_col] == None:
                    valid_moves.append((new_row, new_col))

                # If same coloured piece is on next tile, end loop
                elif board[new_row][new_col].colour == self.colour:
                    break

                # If opposing piece on next tile, add capture move and end loop
                elif board[new_row][new_col].colour == self.opp_colour:
                    valid_moves.append((new_row, new_col))
                    break
    
        return valid_moves