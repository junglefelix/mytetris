"""
Game logic functions for Tetris
This file contains helper functions for game mechanics
"""

def is_valid_position(grid, piece):
    """
    Check if a piece can be placed at its current position
    Returns True if valid, False if collision
    """
    # TODO: Your son can implement collision detection here!
    # Hints:
    # - Check if piece is within grid boundaries
    # - Check if piece overlaps with existing blocks
    # - Use piece.get_cells() to get all occupied cells
    for x, y in piece.get_cells():
        # Check boundaries
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            return False
        # Check collision with existing blocks
        if grid[y][x] != 0:
            return False
    return True  # Placeholder, implement actual logic

def place_piece(grid, piece):
    """
    Place a piece permanently on the grid
    """
    for x, y in piece.get_cells():
        if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
            grid[y][x] = piece.color  # Or use a number representing the piece type

def clear_lines(grid):
    """
    Clear completed lines and return number of lines cleared
    """
    # TODO: Your son can implement line clearing here!
    # Hints:
    # - Check each row to see if it's completely filled
    # - Remove filled rows
    # - Add empty rows at the top
    # - Return the number of lines cleared for scoring
    lines_cleared = 0
    new_grid = []
    for row in grid:
        if all(cell != 0 for cell in row):
            lines_cleared += 1
        else:
            new_grid.append(row)
    # Add empty rows at the top 
    for _ in range(lines_cleared):
        new_grid.insert(0, [0] * len(grid[0]))
    # Update the grid
    for i in range(len(grid)):
        grid[i] = new_grid[i] if i < len(new_grid) else [0] * len(grid[0])  
    return lines_cleared

def calculate_score(lines_cleared, level):
    """
    Calculate score based on lines cleared and current level
    """
    # Standard Tetris scoring
    points = {
        1: 100,
        2: 300,
        3: 500,
        4: 800  # Tetris!
    }
    
    if lines_cleared in points:
        return points[lines_cleared] * level
    return 0
