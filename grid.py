import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.cell_colors = Colors.get_cell_colors()

    def print_grid(self):
        for _rows_ in range(self.num_rows):
            for _cols_ in range(self.num_cols):
                print(self.grid[_rows_][_cols_],end=" ")
            print()
    
    # for drawing cells in the displaying screen
    def draw(self, screen):
        for _rows_ in range(self.num_rows):
            for _cols_ in range(self.num_cols):
                cell_value = self.grid[_rows_][_cols_]
                cell_rectangle = pygame.Rect(_cols_*self.cell_size, _rows_*self.cell_size, self.cell_size-1, self.cell_size-1)  # Rect(x coordinate, y coordinate, width, height)
                
                # pygame.draw.rect(surface  to draw on, color, rectangle) method to draw the cells
                pygame.draw.rect(screen, self.cell_colors[cell_value], cell_rectangle)