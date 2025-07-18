import pygame
import random
import sys

from pieces import TetrisPiece

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 28
GRID_X_OFFSET = 50
GRID_Y_OFFSET = 30

# Colors (RGB values)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)

# Tetris piece colors
PIECE_COLORS = [CYAN, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED]

class TetrisGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Tetris - Learn Python with Dad!")
        self.clock = pygame.time.Clock()
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.running = True
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.current_piece = TetrisPiece('T')
        
    def draw_grid(self):
        """Draw the game grid"""
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                rect = pygame.Rect(
                    GRID_X_OFFSET + x * CELL_SIZE,
                    GRID_Y_OFFSET + y * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
                
                # Draw filled cells
                if self.grid[y][x] != 0:
                    pygame.draw.rect(self.screen, PIECE_COLORS[self.grid[y][x] - 1], rect)
                
                # Draw grid lines
                pygame.draw.rect(self.screen, WHITE, rect, 1)
    
    def draw_score(self):
        """Draw the current score"""
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (WINDOW_WIDTH - 200, 50))
    
    def handle_events(self):
        """Handle game events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.current_piece.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.current_piece.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    self.current_piece.move(0, 1)
               
        pass
    
    def update(self):
        """Update game state"""
        
        # TODO: Add game logic here
        # Your son can implement piece movement, line clearing, etc.
        pass
    
    def draw(self):
        """Draw everything on screen"""
        self.screen.fill(BLACK)
        self.draw_grid()
        self.draw_score()

        # Draw the current piece
        cells = self.current_piece.get_cells()
        for cell in cells:
            x, y = cell
            if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:  # Only draw if within bounds
                rect = pygame.Rect(
                    GRID_X_OFFSET + x * CELL_SIZE,
                    GRID_Y_OFFSET + y * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
                # Draw the piece with a bright color and border
                pygame.draw.rect(self.screen, PIECE_COLORS[self.current_piece.color - 1], rect)
                pygame.draw.rect(self.screen, WHITE, rect, 2)  # White border to make it visible
        
        # Draw instructions
        instructions = [
            "Controls to add:",
            "← Move left",
            "→ Move right", 
            "↓ Move down fast",
            "↑ Rotate piece"
        ]
        
        for i, instruction in enumerate(instructions):
            text = self.font.render(instruction, True, WHITE)
            self.screen.blit(text, (400, 150 + i * 30))
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = TetrisGame()
    game.run()
