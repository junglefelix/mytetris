"""
Tetris piece shapes and their rotations
This file contains the definitions for all 7 standard Tetris pieces
"""

# Tetris piece shapes (represented as 2D arrays)
# 0 = empty, 1 = filled
PIECES = {
    'I': [
        [[1, 1, 1, 1]]
    ],
    'O': [
        [[1, 1],
         [1, 1]]
    ],
    'T': [
        [[0, 1, 0],
         [1, 1, 1]]
    ],
    'S': [
        [[0, 1, 1],
         [1, 1, 0]]
    ],
    'Z': [
        [[1, 1, 0],
         [0, 1, 1]]
    ],
    'J': [
        [[1, 0, 0],
         [1, 1, 1]]
    ],
    'L': [
        [[0, 0, 1],
         [1, 1, 1]]
    ]
}

class TetrisPiece:
    def __init__(self, piece_type, GRID_WIDTH=10):
        self.type = piece_type
        self.GRID_WIDTH= GRID_WIDTH
        self.shape = PIECES[piece_type][0]  # Start with first rotation
        self.x = 4  # Start in middle of grid
        self.y = 1  # Start one row down to be more visible
        self.color = list(PIECES.keys()).index(piece_type) + 1
    
    def rotate(self):
        """Rotate the piece 90 degrees clockwise"""
        # TODO: Your son can implement piece rotation here!
        # Hint: To rotate a 2D array 90 degrees clockwise,
        # the new array[i][j] = old array[len-1-j][i]
        self.shape = [list(row) for row in zip(*self.shape[::-1])]
        pass
    
    def move(self, dx, dy):
        """Move the piece by dx, dy"""
        if dx < 0 and self.x + dx < 0:
            return
        if dx > 0 and self.x + dx + len(self.shape[0]) >self.GRID_WIDTH:
            return  
        #if dy > 0 and self.y + dy + len(self.shape) > GRID_HEIGHT:
        #   return
        self.x += dx
        self.y += dy
    
    def get_cells(self):
        """Get all cells occupied by this piece"""
        cells = []
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    cells.append((self.x + x, self.y + y))
        return cells
    def copy(self):
        import copy
        return copy.deepcopy(self)
    
